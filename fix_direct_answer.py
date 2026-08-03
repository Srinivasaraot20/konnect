import re

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

new_section = '''
    <!-- Direct Answer / Conversational Query Section -->
    <section class="py-5 bg-white" id="how-to-buy">
      <div class="container-fluid max-w-4xl px-3 px-md-4 py-md-3">
        <div class="text-center mx-auto mb-4">
          <h2 class="section-title mb-3" style="font-size: clamp(1.8rem, 3vw, 2.2rem);">
            How to Buy Property in Hyderabad?
          </h2>
          <p class="mb-4" style="color: var(--gray); font-size: 1.05rem; line-height: 1.7; text-align: left;">
            <strong>To buy a property in Hyderabad, you should first identify your investment goal (residential or commercial), set a clear budget, and choose a high-growth location like West Hyderabad or emerging DTCP zones. Most importantly, always verify the property's legal titles and RERA/HMDA approvals.</strong>
          </p>
        </div>
        <div class="row">
          <div class="col-12 text-start">
            <h3 class="fw-bold mb-3" style="font-size: 1.25rem; color: var(--royal-blue-dark);">Step-by-Step Property Buying Guide</h3>
            <ul class="list-unstyled d-flex flex-column gap-3">
              <li class="d-flex gap-3">
                <i class="fas fa-search" style="color: var(--gold); margin-top: 4px;"></i>
                <div>
                  <strong>Step 1: Explore Properties</strong> - Browse our <a href="#properties" class="text-decoration-underline text-dark">curated properties</a> to find verified villas and plots.
                </div>
              </li>
              <li class="d-flex gap-3">
                <i class="fas fa-file-signature" style="color: var(--gold); margin-top: 4px;"></i>
                <div>
                  <strong>Step 2: Legal Verification</strong> - We ensure 100% legal compliance and clear titles before you make a commitment.
                </div>
              </li>
              <li class="d-flex gap-3">
                <i class="fas fa-handshake" style="color: var(--gold); margin-top: 4px;"></i>
                <div>
                  <strong>Step 3: Registration & Handover</strong> - Complete the registration process seamlessly with our <a href="#contact" class="text-decoration-underline text-dark">expert consultants</a>.
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
'''

content = content.replace('    <!-- FAQ -->', new_section)

with open('c:/Users/ASUS/Downloads/rekonnect1/rekonnect/core/templates/core/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
