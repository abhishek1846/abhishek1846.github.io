from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Frame, PageTemplate

class ResumeDocTemplate(SimpleDocTemplate):
    def build(self, flowables, onFirstPage=None, onLaterPages=None, canvasmaker=None):
        self._calc()
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id='normal',
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0
        )
        self.addPageTemplates([
            PageTemplate(id='First', frames=frame, pagesize=self.pagesize),
            PageTemplate(id='Later', frames=frame, pagesize=self.pagesize)
        ])
        super(SimpleDocTemplate, self).build(flowables)

def build_pdf(filename):
    left_margin = 46
    right_margin = 46
    printable_width = 595.28 - (left_margin + right_margin) # 503.28 pt

    doc = ResumeDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=36,
        bottomMargin=32
    )

    link_color = "#1d4ed8"

    name_style = ParagraphStyle(
        'Name',
        fontName='Helvetica-Bold',
        fontSize=21,
        leading=24,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=3
    )

    header_sub_style = ParagraphStyle(
        'HeaderSub',
        fontName='Helvetica',
        fontSize=10,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=1.5
    )

    section_title_style = ParagraphStyle(
        'SectionTitle',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=6,
        spaceAfter=2
    )

    body_text_style = ParagraphStyle(
        'BodyText',
        fontName='Helvetica',
        fontSize=10,
        leading=13.8,
        textColor=colors.HexColor('#1e293b')
    )

    company_style = ParagraphStyle(
        'Company',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#0f172a')
    )

    date_style = ParagraphStyle(
        'Date',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=2,
        textColor=colors.HexColor('#475569')
    )

    subrole_style = ParagraphStyle(
        'Subrole',
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#475569')
    )

    bullet_text_style = ParagraphStyle(
        'BulletText',
        fontName='Helvetica',
        fontSize=10,
        leading=13.8,
        textColor=colors.HexColor('#1e293b')
    )

    bullet_symbol_style = ParagraphStyle(
        'BulletSymbol',
        fontName='Helvetica',
        fontSize=10,
        leading=13.8,
        alignment=0,
        textColor=colors.HexColor('#475569')
    )

    def hr():
        return HRFlowable(
            width="100%",
            thickness=0.6,
            color=colors.HexColor('#0f172a'),
            spaceBefore=1,
            spaceAfter=5,
            hAlign='LEFT'
        )

    def make_header_row(left_text, right_text):
        lp = Paragraph(left_text, company_style)
        rp = Paragraph(right_text, date_style)
        t = Table([[lp, rp]], colWidths=[370, printable_width - 370], hAlign='LEFT')
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        return t

    def make_bullet(text_html):
        bp = Paragraph("•", bullet_symbol_style)
        tp = Paragraph(text_html, bullet_text_style)
        t = Table([[bp, tp]], colWidths=[14, printable_width - 14], hAlign='LEFT')
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ]))
        return t

    story = []

    # 1. Header with hyperlinked personal portfolio and LinkedIn in subtle blue
    story.append(Paragraph("Abhishek Singh", name_style))
    story.append(Paragraph("Staff Product Manager | AI-powered B2B SaaS: identity security, data and analytics | Bengaluru, India", header_sub_style))
    story.append(Paragraph(
        f'<a href="https://abhishek1846.github.io" color="{link_color}">abhishek1846.github.io</a> &nbsp;|&nbsp; '
        f'<a href="https://www.linkedin.com/in/abhishek1846" color="{link_color}">linkedin.com/in/abhishek1846</a>',
        header_sub_style
    ))
    story.append(Spacer(1, 2))

    # 2. Summary
    story.append(Paragraph("SUMMARY", section_title_style))
    story.append(hr())
    story.append(Paragraph(
        "Staff PM with ~10 years across analytics, healthcare data and enterprise security. "
        "Leads product for Non-Human Identity (NHI) and AI agent governance at Oleria, "
        "setting direction across three engineering teams and partnering with Fortune 500 enterprise customers. "
        "Two-time founder.",
        body_text_style
    ))
    story.append(Spacer(1, 4))

    # 3. Experience
    story.append(Paragraph("EXPERIENCE", section_title_style))
    story.append(hr())

    # Oleria
    story.append(make_header_row(f'<b><a href="https://oleria.com" color="{link_color}">Oleria</a></b>', "May 2025 - Present"))

    role_sub_table = Table([[
        Paragraph("<b>Staff Product Manager</b> (Aug 2026 - Present) &nbsp;&nbsp;|&nbsp;&nbsp; <b>Senior Product Manager</b> (May 2025 - Aug 2026)", body_text_style),
    ]], colWidths=[printable_width], hAlign='LEFT')
    role_sub_table.setStyle(TableStyle([
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(role_sub_table)

    first_pm_table = Table([[
        Paragraph("First Product Manager in India; sole PM across a ~30-engineer organization", subrole_style)
    ]], colWidths=[printable_width], hAlign='LEFT')
    first_pm_table.setStyle(TableStyle([
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(first_pm_table)

    story.append(make_bullet("Lead product for Non-Human Identity (NHI) and AI agent governance, now the company's core strategic focus; primary focus of new pipeline."))
    story.append(make_bullet("Drove $3M in net new PoCs now at advanced procurement stage by repositioning product and customer conversations around NHI and AI governance."))
    story.append(make_bullet("Led AI agent governance: continuous discovery of agents across Gemini Enterprise, Salesforce Agentforce, AWS Bedrock and Entra/Copilot, mapped to humans on the identity graph with reviews and remediation."))
    story.append(make_bullet("Shaped the Oleria MCP/AI experience: an AI identity security expert that answers customer questions on their actual data by querying the full context graph."))
    story.append(make_bullet("Own NHI discovery, access reviews, Workflow Studio and Integration Studio; expanded the integration catalog from 20 to 200+ applications."))
    story.append(make_bullet("Mentor engineering to think like product engineers and represent Oleria at industry security conferences."))
    story.append(Spacer(1, 4))

    # Kloudfuse
    story.append(make_header_row(f'<b><a href="https://kloudfuse.com" color="{link_color}">Kloudfuse</a></b> - Product Growth Lead, India', "Apr 2024 - May 2025"))
    story.append(Spacer(1, 1))
    story.append(make_bullet("Opened the India market; onboarded 1mg, Innovaccer and GE Health."))
    story.append(make_bullet("Led the launch of Real User Monitoring (RUM) and other product updates."))
    story.append(make_bullet("Grew the India team from 3 to 8 across 2024-2025."))
    story.append(Spacer(1, 4))

    # Komma & Dashh
    story.append(make_header_row("<b>Co-Founder / CEO - Komma and Dashh</b>", "Dec 2021 - Feb 2024"))
    story.append(Spacer(1, 1))
    story.append(make_bullet("<b>Komma:</b> built collaborative analytics notebooks for data teams after 150+ interviews with data leaders (Twilio, United Airlines); 6 PoC customers, $150K pre-seed."))
    story.append(make_bullet("<b>Dashh:</b> built 1-click checkout for e-commerce; led product, design and GTM; turned down two acquihire offers."))
    story.append(Spacer(1, 4))

    # PharmEasy
    story.append(make_header_row(f'<b><a href="https://pharmeasy.in" color="{link_color}">PharmEasy</a></b> - Product Manager', "Nov 2018 - Nov 2021"))
    story.append(Spacer(1, 1))
    story.append(make_bullet("Owned the roadmap for Docon, a digital prescription platform acquired by PharmEasy: about 1M prescriptions per month, feeding its e-pharmacy and diagnostics businesses."))
    story.append(make_bullet("Additionally built prescription analytics for pharma companies and doctor-facing analytics dashboards."))
    story.append(Spacer(1, 4))

    # ZS Associates
    story.append(make_header_row(f'<b><a href="https://zs.com" color="{link_color}">ZS Associates</a></b> - Decision Analytics Associate', "Jun 2017 - Oct 2018"))
    story.append(Spacer(1, 1))
    story.append(make_bullet("Worked directly with US clients; the only first-year associate on the team to train new joiners."))
    story.append(Spacer(1, 4))

    # Education and Publications on separate lines
    story.append(Paragraph("EDUCATION AND PUBLICATIONS", section_title_style))
    story.append(hr())
    story.append(make_header_row("<b>IIT (BHU), Varanasi</b> - B.Tech + M.Tech in Engineering", "2012 - 2017"))
    story.append(Spacer(1, 3.5))
    story.append(make_header_row(
        f'<b>Co-author, <a href="https://www.dsci.in/resource/content/identity-security-maturity-ai-era" color="{link_color}"><i>Identity Security Maturity in the AI Era</i></a></b>',
        "DSCI (with Oleria)"
    ))

    doc.build(story)

if __name__ == "__main__":
    targets = [
        "/Users/abhisheksingh/Downloads/Abhishek Singh Resume.pdf",
        "/Users/abhisheksingh/Projects/portfolio/public/resume.pdf"
    ]
    for target in targets:
        build_pdf(target)
        print("Generated:", target)
