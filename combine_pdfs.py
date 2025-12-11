#!/usr/bin/env python3
"""
Combine all memos into a single PDF compilation
"""

import os
from PyPDF2 import PdfMerger, PdfReader
from PIL import Image
import io


def convert_image_to_pdf_bytes(image_path):
    """Convert image to PDF bytes"""
    img = Image.open(image_path)
    # Convert to RGB if necessary
    if img.mode in ("RGBA", "LA", "P"):
        background = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        background.paste(
            img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None
        )
        img = background

    # Save to bytes
    pdf_bytes = io.BytesIO()
    img.save(pdf_bytes, format="PDF", resolution=100.0)
    pdf_bytes.seek(0)
    return pdf_bytes


def main():
    memos_dir = "memos"
    output_file = "memos/great-memos-compilation.pdf"

    # List of memos in order (by category as shown on the site)
    memo_files = [
        # Historical & Political Documents
        "pliny-trajan-christians.pdf",
        "washington-states.pdf",
        "carp-nuclear.pdf",
        "powell-memo.pdf",
        "shultz-reagan.pdf",
        # Strategic Memos & Leadership
        "churchill-brevity.jpg",
        "garlinghouse-peanut-butter.pdf",
        "hinkie-76rs.pdf",
        "slack-saddles.pdf",
        "schultz-strategic.pdf",
        "zuck-messenger-ecosystem.pdf",
        "zuck-systrom.pdf",
        "jeff-disney.pdf",
        "mtv.pdf",
        "kilar-hulu.pdf",
        "ogilvy-principles.jpeg",
        # Tech Leadership & Product Philosophy
        "jobs-ibooks.pdf",
        "musk-tesla.png",
        "billgates-moviemaker.pdf",
        "billgates-tidalwave.pdf",
        "yegge.pdf",
        "javier-showrunning.pdf",
        "completed-staff-work-thomas-watson-jr-ibm.pdf",
        "jackson-word.pdf",
        "zerodef.pdf",
        "nate-roadkill.pdf",
        "ozzie-internet.pdf",
        "bosworth-ads.pdf",
        "zuck-unity.pdf",
        "sutton-bitter-lesson.pdf",
        # Investment & Business Analysis
        "buffett-geico.pdf",
        "buffett-sees.pdf",
        "buffett-raikes-emails.pdf",
        "markopolos-madoff-fraud.pdf",
        "roelof-youtube.pdf",
        "bessemer-yelp.pdf",
        "besssemer-linkedin.pdf",
        "bessemer-lifelock.pdf",
        "bessemer-wix.pdf",
        "bessemer-dropcam.pdf",
        "bessemer-twilio.pdf",
        "bessemer-mindbody.pdf",
        "bessemer-shopify.pdf",
        "bessemer-mediassist.pdf",
        "bessemer-fiverr.pdf",
        "bessemer-pinterest.pdf",
        "bessemer-sendgrid.pdf",
        "bessemer-twitch.pdf",
        "smith-goldman.pdf",
        "bessemer-auth0.pdf",
        "bessemer-pagerduty.pdf",
        "bessemer-rocketlab.pdf",
        "bessemer-servicetitan.pdf",
        "bessemer-velo3d.pdf",
        "bessemer-toast.pdf",
    ]

    merger = PdfMerger()

    print("Combining memos into single PDF...")

    for memo_file in memo_files:
        file_path = os.path.join(memos_dir, memo_file)

        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found, skipping...")
            continue

        print(f"Adding: {memo_file}")

        # Handle images separately
        if memo_file.endswith((".jpg", ".jpeg", ".png")):
            pdf_bytes = convert_image_to_pdf_bytes(file_path)
            merger.append(pdf_bytes)
        else:
            merger.append(file_path)

    # Write the combined PDF
    print(f"\nWriting combined PDF to: {output_file}")
    merger.write(output_file)
    merger.close()

    print("Done! Compilation created successfully.")

    # Print file size
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    print(f"File size: {file_size:.2f} MB")


if __name__ == "__main__":
    main()
