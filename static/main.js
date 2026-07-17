document.addEventListener('DOMContentLoaded', () => {
  // Set current year
  document.getElementById('year').textContent = new Date().getFullYear();

  // Loading Screen
  setTimeout(() => {
    const loader = document.getElementById('loadingScreen');
    if(loader) {
      loader.classList.add('hide');
      setTimeout(() => loader.remove(), 600);
    }
  }, 1800);

  // Initialize AOS
  AOS.init({
    once: true,
    offset: 50,
    duration: 800,
    easing: 'ease-out-cubic'
  });

  // Scroll Progress & Navbar Scrolled state
  const scrollProgress = document.getElementById('scroll-progress');
  const navbar = document.getElementById('navbar');
  const backToTop = document.getElementById('backToTop');
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');

  const scrollHandler = () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    
    if (scrollProgress) scrollProgress.style.width = progress + '%';
    
    if (scrollTop > 60) {
      navbar.classList.add('scrolled');
      backToTop.classList.remove('d-none');
    } else {
      navbar.classList.remove('scrolled');
      backToTop.classList.add('d-none');
    }

    // Active link updating
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (scrollY >= sectionTop - 150) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  };
  window.addEventListener('scroll', scrollHandler, { passive: true });

  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      if(this.getAttribute('href') === '#') return;
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetEl = document.getElementById(targetId);
      if(targetEl) {
        window.scrollTo({
          top: targetEl.offsetTop - 70, // offset for navbar
          behavior: 'smooth'
        });
      }
    });
  });
  
  if (backToTop) {
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Mobile Menu Toggle
  const menuToggle = document.getElementById('menuToggle');
  const menuClose = document.getElementById('menuClose');
  const mobileMenu = document.getElementById('mobileMenu');
  
  if (menuToggle && menuClose && mobileMenu) {
    const toggleMenu = () => mobileMenu.classList.toggle('open');
    menuToggle.addEventListener('click', toggleMenu);
    menuClose.addEventListener('click', toggleMenu);
    
    // Close menu on link click
    document.querySelectorAll('.mobile-nav-link').forEach(link => {
      link.addEventListener('click', () => mobileMenu.classList.remove('open'));
    });
    document.getElementById('mobileConsult')?.addEventListener('click', () => mobileMenu.classList.remove('open'));
    
    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('open')) {
        mobileMenu.classList.remove('open');
      }
    });

    // Close on click outside
    document.addEventListener('click', (e) => {
      if (mobileMenu.classList.contains('open') && !mobileMenu.contains(e.target) && !menuToggle.contains(e.target)) {
        mobileMenu.classList.remove('open');
      }
    });
  }

  // Data
  const properties = [
    {
      title: 'Luxury Villas',
      alt: 'Luxury Villa in Hyderabad',
      desc: 'Premium gated-community villas with world-class amenities in Hyderabad\'s finest neighborhoods.',
      img: 'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=300',
    },
    {
      title: 'Premium Apartments',
      alt: 'Premium Apartment in Hyderabad',
      desc: 'Spacious, modern apartments in prime locations with excellent connectivity and lifestyle features.',
      img: 'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=300',
    },
    {
      title: 'Commercial Spaces',
      alt: 'Commercial Office Space in Hyderabad',
      desc: 'High-return office spaces and retail outlets in Hyderabad\'s booming business districts.',
      img: 'https://images.pexels.com/photos/302769/pexels-photo-302769.jpeg?auto=compress&cs=tinysrgb&w=300',
    },
    {
      title: 'Open Plots',
      alt: 'HMDA Approved Open Plot',
      desc: 'Strategically selected plots with strong appreciation potential across Telangana and Andhra Pradesh.',
      img: 'https://images.pexels.com/photos/210487/pexels-photo-210487.jpeg?auto=compress&cs=tinysrgb&w=300',
    },
    {
      title: 'Independent Houses',
      alt: 'Independent House in Hyderabad',
      desc: 'Quality independent homes offering comfort, privacy, and long-term value for families.',
      img: 'https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=300',
    },
  ];

  const propertyDetails = {
    'Luxury Villas': {
      description: "Discover premium gated-community villas located in Hyderabad's most prestigious neighborhoods.",
      gallery: [
        'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/208736/pexels-photo-208736.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/1643384/pexels-photo-1643384.jpeg?auto=compress&cs=tinysrgb&w=300'
      ],
      sections: [
        { title: 'Features', icon: '<i class="fas fa-star"></i>', items: ['3 BHK, 4 BHK & 5 BHK Villas', 'Gated Communities', 'Clubhouse & Swimming Pool', 'Landscaped Gardens', 'Bank Loan Assistance'] },
        { title: 'Amenities', icon: '<i class="fas fa-swimmer"></i>', items: ['Children\'s Play Area', 'Gym & Indoor Games', '24×7 Security', 'Premium Construction Quality', 'Power Backup'] }
      ],
      whyChoose: "Unmatched luxury, exclusive communities, and premium lifestyle amenities in serene environments."
    },
    'Premium Apartments': {
      description: "Modern apartments designed for luxury living with excellent connectivity.",
      gallery: [
        'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/439391/pexels-photo-439391.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/276724/pexels-photo-276724.jpeg?auto=compress&cs=tinysrgb&w=300'
      ],
      sections: [
        { title: 'Features', icon: '<i class="far fa-building"></i>', items: ['2 BHK, 3 BHK, 4 BHK', 'High-rise Towers', 'Clubhouse', 'Swimming Pool'] },
        { title: 'Amenities', icon: '<i class="fas fa-shield-alt"></i>', items: ['Gym', 'Children\'s Park', 'Covered Parking', 'Smart Security', 'Near Metro & IT Hubs'] }
      ],
      whyChoose: "Perfect balance of urban convenience, top-tier security, and vibrant community living."
    },
    'Commercial Spaces': {
      description: "High-return commercial investment opportunities.",
      gallery: [
        'https://images.pexels.com/photos/302769/pexels-photo-302769.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/380768/pexels-photo-380768.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/267507/pexels-photo-267507.jpeg?auto=compress&cs=tinysrgb&w=300'
      ],
      sections: [
        { title: 'Available Properties', icon: '<i class="fas fa-briefcase"></i>', items: ['Office Spaces', 'Retail Shops', 'IT Office Floors', 'Commercial Buildings', 'Showrooms', 'Food Court Spaces'] }
      ],
      whyChoose: "Strategic locations that guarantee high footfall, excellent visibility, and outstanding rental yields."
    },
    'Open Plots': {
      description: "Verified investment plots with excellent appreciation potential.",
      gallery: [
        'https://images.pexels.com/photos/210487/pexels-photo-210487.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/1105754/pexels-photo-1105754.jpeg?auto=compress&cs=tinysrgb&w=300'
      ],
      sections: [
        { title: 'Plot Sizes', icon: '<i class="fas fa-expand"></i>', items: ['150 Sq. Yards', '200 Sq. Yards', '300 Sq. Yards', '400+ Sq. Yards'] },
        { title: 'Benefits', icon: '<i class="fas fa-chart-line"></i>', items: ['DTCP Approved', 'HMDA Approved', 'Bank Loan Available', 'Clear Titles', 'Immediate Registration', 'High Appreciation'] }
      ],
      whyChoose: "Secure your financial future with fast-appreciating land in rapidly developing corridors."
    },
    'Independent Houses': {
      description: "Beautiful independent homes offering privacy, comfort, and long-term value.",
      gallery: [
        'https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=300',
        'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=300'
      ],
      sections: [
        { title: 'Features', icon: '<i class="fas fa-home"></i>', items: ['2 BHK & 3 BHK', 'Duplex Houses', 'Triplex Houses', 'Parking', 'Loan Assistance'] },
        { title: 'Amenities', icon: '<i class="fas fa-couch"></i>', items: ['Modern Interiors', 'Modular Kitchen', 'Terrace'] }
      ],
      whyChoose: "Complete privacy, zero maintenance fees, and the freedom to customize your own living space."
    }
  };

  const testimonials = [
    { name: 'Rajesh Kumar', location: 'Hyderabad, Telangana', text: 'Shravan Kumar made our property purchase smooth and stress-free. His guidance and transparency gave us complete confidence throughout the process.', img: 'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&w=150', rating: 5 },
    { name: 'Priya Sharma', location: 'Visakhapatnam, AP', text: 'Our commercial investment exceeded expectations thanks to Shravan\'s market knowledge and professional advice. Highly recommended for any property investment.', img: 'https://images.pexels.com/photos/1239291/pexels-photo-1239291.jpeg?auto=compress&cs=tinysrgb&w=150', rating: 5 },
    { name: 'Venkat Reddy', location: 'Warangal, Telangana', text: 'I was looking for an open plot for investment. Shravan sir guided me to a location that has already appreciated by 40% in two years. Genuine consultant.', img: 'https://images.pexels.com/photos/697509/pexels-photo-697509.jpeg?auto=compress&cs=tinysrgb&w=150', rating: 5 },
    { name: 'Anita Desai', location: 'Hyderabad, Telangana', text: 'As a first-time buyer, I was nervous about the process. The team at Konnect Projects handled everything from legal verification to documentation. Truly professional.', img: 'https://images.pexels.com/photos/1212984/pexels-photo-1212984.jpeg?auto=compress&cs=tinysrgb&w=150', rating: 5 },
    { name: 'Suresh Babu', location: 'Vijayawada, AP', text: 'Bought a premium apartment through Konnect Projects. The entire process was transparent, and I got a great deal. Will definitely refer friends and family.', img: 'https://images.pexels.com/photos/1043471/pexels-photo-1043471.jpeg?auto=compress&cs=tinysrgb&w=150', rating: 5 },
    { name: 'Lakshmi Narayana', location: 'Hyderabad, Telangana', text: 'Exceptional service and deep market knowledge. Shravan Kumar understands the real estate landscape in Telangana and AP like no one else. A trusted partner.', img: 'https://images.pexels.com/photos/1222271/pexels-photo-1222271.jpeg?auto=compress&cs=tinysrgb&w=150', rating: 5 }
  ];

  const faqs = [
    { q: 'Do you provide legally verified properties?', a: 'Yes. Every property we list goes through a thorough legal verification process. We ensure clear titles, proper documentation, and compliance with local regulations before presenting any property to our clients.' },
    { q: 'Which locations do you cover?', a: 'We primarily cover Telangana and Andhra Pradesh, with a strong focus on Hyderabad, Warangal, Visakhapatnam, Vijayawada, and surrounding growth corridors. Our network extends across both states.' },
    { q: 'Do you help first-time buyers?', a: 'Absolutely. We specialize in guiding first-time buyers through every step of the process — from understanding the market and selecting the right property to legal verification, documentation, and final registration.' },
    { q: 'Can you assist with investment properties?', a: 'Yes. With 15+ years of market experience, we provide personalized investment guidance tailored to your financial goals. We identify properties with strong appreciation potential and rental yield across both states.' },
    { q: 'What types of properties do you deal in?', a: 'We cover luxury villas, premium apartments, commercial spaces, open plots, and independent houses. Our portfolio spans every major property category to serve diverse client needs.' },
    { q: 'How do I schedule a consultation?', a: 'You can book a free consultation by clicking the "Book Free Consultation" button, calling us directly, or messaging us on WhatsApp. We\'ll schedule a convenient time to discuss your property requirements.' },
  ];

  // Render Properties
  const propList = document.getElementById('propertiesList');
  if (propList) {
    properties.forEach((p, i) => {
      const delay = i * 100;
      const html = `
        <div class="col-12 col-md-6 col-lg-4 col-xl-3" data-aos="fade-up" data-aos-delay="${delay}">
          <div class="prop-card">
            <img src="${p.img}" alt="${p.alt}" width="400" height="250" loading="lazy" decoding="async">
            <div class="prop-card-overlay">
              <h3 style="font-family: 'Poppins'; font-weight: 700; font-size: 1.15rem; color: #fff; margin-bottom: 6px;">${p.title}</h3>
              <p style="color: rgba(255,255,255,0.8); font-size: 0.85rem; line-height: 1.6; margin-bottom: 12px;">${p.desc}</p>
              <button class="prop-explore-btn" onclick="expandProperty('${p.title}')">
                Explore <i class="fas fa-arrow-right fs-xs"></i>
              </button>
            </div>
          </div>
        </div>
      `;
      propList.insertAdjacentHTML('beforeend', html);
    });

    // Append CTA
    const ctaHtml = `
      <div class="col-12 col-md-6 col-lg-4 col-xl-3" data-aos="fade-up" data-aos-delay="500">
        <div class="rounded-4 d-flex flex-column align-items-center justify-content-center p-4 text-center h-100" style="background: linear-gradient(135deg, var(--royal-blue), var(--royal-blue-light)); min-height: 240px;">
          <h3 style="font-family: 'Poppins'; font-weight: 700; font-size: 1.3rem; color: #fff; margin-bottom: 8px;">Can't Find What You're Looking For?</h3>
          <p style="color: rgba(255,255,255,0.75); font-size: 0.85rem; margin-bottom: 20px;">Tell us your requirements and we'll find the perfect match.</p>
          <a href="#contact" class="btn-gold text-decoration-none">Book Consultation</a>
        </div>
      </div>
    `;
    propList.insertAdjacentHTML('beforeend', ctaHtml);
  }

  // Render Testimonials
  const testList = document.getElementById('testimonialsList');
  if (testList) {
    testimonials.forEach(t => {
      const stars = Array(t.rating).fill('<i class="fas fa-star" style="color: var(--gold-light);"></i>').join('');
      const html = `
        <div class="swiper-slide">
          <div class="testi-card">
            <i class="fas fa-quote-left fa-2x" style="color: var(--gold); opacity: 0.6; margin-bottom: 12px;"></i>
            <div class="d-flex gap-1 mb-3">${stars}</div>
            <p style="color: rgba(255,255,255,0.85); font-size: 0.9rem; line-height: 1.8; margin-bottom: 20px; min-height: 120px;">
              "${t.text}"
            </p>
            <div class="d-flex align-items-center gap-3">
              <img src="${t.img}" alt="Client Testimonial ${t.name}" width="48" height="48" class="rounded-circle object-fit-cover" style="width: 48px; height: 48px; border: 2px solid var(--gold);" loading="lazy" decoding="async">
              <div>
                <div style="font-family: 'Poppins'; font-weight: 600; font-size: 0.9rem; color: #fff;">${t.name}</div>
                <div style="font-size: 0.78rem; color: var(--gold-light);">${t.location}</div>
              </div>
            </div>
          </div>
        </div>
      `;
      testList.insertAdjacentHTML('beforeend', html);
    });

    // Init Swiper
    new Swiper(".testimonialsSwiper", {
      slidesPerView: 1,
      spaceBetween: 24,
      loop: false,
      navigation: {
        nextEl: ".swiper-button-next-custom",
        prevEl: ".swiper-button-prev-custom",
      },
      pagination: {
        el: ".swiper-pagination-custom",
        clickable: true,
      },
      breakpoints: {
        768: { slidesPerView: 2 },
        1024: { slidesPerView: 3 },
      },
    });
  }

  // Render FAQs
  const faqContainer = document.getElementById('faqAccordion');
  if (faqContainer) {
    faqs.forEach((f, i) => {
      const isExpanded = i === 0;
      const html = `
        <div class="accordion-item border-0">
          <h2 class="accordion-header">
            <button class="accordion-button ${isExpanded ? '' : 'collapsed'}" type="button" data-bs-toggle="collapse" data-bs-target="#faq${i}">
              ${f.q}
            </button>
          </h2>
          <div id="faq${i}" class="accordion-collapse collapse ${isExpanded ? 'show' : ''}" data-bs-parent="#faqAccordion">
            <div class="accordion-body">
              ${f.a}
            </div>
          </div>
        </div>
      `;
      faqContainer.insertAdjacentHTML('beforeend', html);
    });
  }

  // WhatsApp Logic
  window.openWhatsApp = function(title) {
    const propertyMessages = {
      'Luxury Villas': `🏡 Hello Konnect Projects,

I'm interested in your Luxury Villas in Hyderabad.

Please share:

✅ Available Luxury Villas
✅ Villa Configurations (3/4/5 BHK)
✅ Floor Plans
✅ Amenities
✅ Project Brochure
✅ Site Visit
✅ Bank Loan Assistance
✅ Legal Documentation

I look forward to your response.

Thank you.`,
      
      'Premium Apartments': `🏢 Hello Konnect Projects,

I'm interested in your Premium Apartments.

Please share the following details:

✅ Available Apartments
✅ 2 BHK / 3 BHK / 4 BHK Options
✅ Floor Plans
✅ Amenities & Features
✅ Project Brochure
✅ Site Visit Availability
✅ Home Loan Assistance
✅ Legal Documentation

Thank you.`,
      
      'Commercial Spaces': `🏢 Hello Konnect Projects,

I'm interested in your Commercial Properties in Hyderabad.

Please share:

✅ Office Spaces
✅ Retail Shops
✅ Commercial Buildings
✅ Business Infrastructure
✅ Investment Benefits
✅ Site Visit
✅ Legal Documentation

Thank you.`,
      
      'Open Plots': `🌱 Hello Konnect Projects,

I'm interested in purchasing an Open Plot.

Please share:

✅ Available Plots
✅ HMDA/DTCP Approved Projects
✅ Plot Layout Brochure
✅ Plot Features
✅ Registration Process
✅ Bank Loan Assistance
✅ Site Visit
✅ Legal Documentation

Thank you.`,
      
      'Independent Houses': `🏡 Hello Konnect Projects,

I'm interested in your Independent Houses in Hyderabad.

Please share:

✅ Available Houses
✅ House Configurations
✅ Floor Plans
✅ Amenities
✅ Project Brochure
✅ Site Visit
✅ Loan Assistance
✅ Legal Documentation

Thank you.`
    };

    const message = propertyMessages[title] || `🏡 Hello Konnect Projects, I'm interested in ${title}. Please share details. Thank you.`;
    window.open(`https://wa.me/919059598777?text=${encodeURIComponent(message)}`, '_blank');
  };

  
  // Expand Property via Modal
  window.expandProperty = function(title) {
    const details = propertyDetails[title];
    if (!details) return;
    
    // Set Badge, Title, Desc
    let badgeText = title.includes('Villa') || title.includes('House') ? 'RESIDENTIAL' : (title.includes('Commercial') ? 'COMMERCIAL' : 'REAL ESTATE');
    document.getElementById('modalPropertyBadge').innerText = badgeText;
    document.getElementById('modalPropertyTitle').innerText = title;
    document.getElementById('modalPropertyDesc').innerText = details.description;
    
    // Set Main Image (use first gallery image)
    if(details.gallery && details.gallery.length > 0) {
      document.getElementById('modalPropertyImg').src = details.gallery[0];
    } else {
      document.getElementById('modalPropertyImg').src = '';
    }
    
    // Map Sections to the specific icon design
    // 💡 Bulb -> Property Overview
    // 🌿 Plant -> Key Features / Why Choose
    // ✅ Check -> Amenities / Specs
    const icons = [
        '<i class="fas fa-lightbulb" style="color: #f5b041; font-size: 1.2rem;"></i>',
        '<i class="fas fa-leaf" style="color: #58d68d; font-size: 1.2rem;"></i>',
        '<i class="fas fa-check-square" style="color: #58d68d; font-size: 1.2rem;"></i>'
    ];
    
    let featuresHtml = details.sections.map((sec, index) => {
        let icon = icons[index % icons.length];
        return `
        <div class="mb-4">
            <h5 class="fw-bold fs-6 d-flex align-items-center gap-2 mb-2" style="color: #1e8449;">
                ${icon} ${sec.title}
            </h5>
            <p class="text-muted m-0 ps-4" style="font-size: 0.9rem; line-height: 1.6;">
                ${sec.items.join(', ')}.
            </p>
        </div>
        `;
    }).join('');
    
    document.getElementById('modalPropertyFeatures').innerHTML = featuresHtml;
    
    // Setup WhatsApp Button
    const waBtn = document.getElementById('modalBtnWhatsApp');
    waBtn.onclick = function() {
        window.openWhatsApp(title);
    };
    
    // Show Modal
    const modal = new bootstrap.Modal(document.getElementById('propertyPopupModal'));
    modal.show();
  };


// Contact Form Submission
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('formName').value;
      const phone = document.getElementById('formPhone').value;
      const email = document.getElementById('formEmail').value;
      const location = document.getElementById('formLocation').value;
      
      const propTypeInput = document.querySelector('input[name="propType"]:checked');
      const propType = propTypeInput ? propTypeInput.value : '';
      
      const budget = document.getElementById('formBudget').value;
      
      const timelineInput = document.querySelector('input[name="timeline"]:checked');
      const timeline = timelineInput ? timelineInput.value : '';
      
      const msg = document.getElementById('formMessage').value;

      const submitData = {
        name, phone, email, location, propType, budget, timeline, message: msg
      };

      fetch('/api/submit-enquiry/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(submitData)
      }).then(res => res.json())
      .then(data => {
        if (data.status === 'success') {
          const waMessage = `🏡 Hello Konnect Projects,

I found your website and I'm interested in purchasing a property.

━━━━━━━━━━━━━━━━━━━━━━
📋 PROPERTY REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━

👤 Name: ${name}

📞 Mobile: ${phone}

🏠 Property Type:
${propType}

📍 Preferred Location:
${location}

💰 Budget:
${budget}

📅 Timeline:
${timeline}

📝 Additional Requirements:
${msg}

━━━━━━━━━━━━━━━━━━━━━━
Please share the best available property options matching my requirements, including:

✅ Property Details
✅ Price & Offers
✅ Location Map
✅ Amenities
✅ Floor Plans
✅ Site Visit Availability
✅ Payment Plans
━━━━━━━━━━━━━━━━━━━━━━

Looking forward to your response.

Thank you,

👤 ${name}`;

          window.open(`https://wa.me/919059598777?text=${encodeURIComponent(waMessage)}`, '_blank');
          
          const successMsg = document.getElementById('formSuccess');
          successMsg.classList.remove('d-none');
          
          setTimeout(() => {
            successMsg.classList.add('d-none');
            contactForm.reset();
          }, 4000);
        } else {
          alert('Error: ' + data.message);
        }
      }).catch(err => {
        alert('An error occurred. Please try again.');
        console.error(err);
      });
    });
  }

  // Newsletter
  const nlForm = document.getElementById('newsletterForm');
  if (nlForm) {
    nlForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const success = document.getElementById('newsletterSuccess');
      success.classList.remove('d-none');
      nlForm.reset();
      setTimeout(() => success.classList.add('d-none'), 3000);
    });
  }



  // Global WhatsApp Button Interceptor
  document.body.addEventListener('click', function(e) {
    const target = e.target.closest('a[href*="wa.me"], #contactWaBtn, #floatWaBtn');
    if (target) {
      // If it's the modal WhatsApp button, we let the existing modal logic handle it, 
      // or we override it. The prompt says "any WhatsApp button". 
      // Let's use the default message if form is empty.
      
      const nameVal = document.getElementById('formName')?.value.trim();
      const phoneVal = document.getElementById('formPhone')?.value.trim();
      
      const propTypeInput = document.querySelector('input[name="propType"]:checked');
      const propTypeVal = propTypeInput ? propTypeInput.value.trim() : '';
      
      const locationVal = document.getElementById('formLocation')?.value.trim();
      const budgetVal = document.getElementById('formBudget')?.value.trim();
      
      const timelineInput = document.querySelector('input[name="timeline"]:checked');
      const timelineVal = timelineInput ? timelineInput.value.trim() : '';
      
      const msgVal = document.getElementById('formMessage')?.value.trim();
      
      let finalMessage = '';
      
      // If form is partially or fully filled, use filled form template
      if (nameVal || phoneVal || propTypeVal || locationVal || budgetVal || timelineVal) {
        finalMessage = `🏡 Hello Konnect Projects,

I visited your website and I'm interested in purchasing a property.

━━━━━━━━━━━━━━━━━━━━━━
📋 PROPERTY REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━

👤 Name: ${nameVal || 'Not provided'}

📞 Mobile: ${phoneVal || 'Not provided'}

🏠 Property Type: ${propTypeVal || 'Not provided'}

📍 Preferred Location: ${locationVal || 'Not provided'}

💰 Budget: ${budgetVal || 'Not provided'}

📅 Timeline: ${timelineVal || 'Not provided'}

📝 Additional Requirements:
${msgVal || 'None'}

━━━━━━━━━━━━━━━━━━━━━━

Please share suitable properties matching my requirements, including:

✅ Property Details
✅ Price Quotation
✅ Brochure
✅ Location Map
✅ Floor Plans
✅ Amenities
✅ Site Visit Availability
✅ Loan Assistance (if available)

Looking forward to your response.

Thank you,
${nameVal || 'User'}`;
      } else {
        // Form is empty, use default message
        finalMessage = `🏡 Hello Konnect Projects,

I visited your website and I'm interested in purchasing a property.

I'm looking for more information about your available properties.

Please share details regarding:

✅ Luxury Villas
✅ Premium Apartments
✅ Commercial Spaces
✅ Open Plots
✅ Independent Houses

Please also share:

• Latest Property Brochure
• Price Details
• Available Locations
• Site Visit Availability
• Payment Plans
• Current Offers

Looking forward to your response.

Thank you.`;
      }

      e.preventDefault();
      window.open(`https://wa.me/919059598777?text=${encodeURIComponent(finalMessage)}`, '_blank');
    }
  });

});
