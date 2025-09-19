status = {
    'meets':
            '''<div class="col-auto">
                    <div class="caption meets">
                                <svg xmlns='http://www.w3.org/2000/svg' height='36px' width='36px' viewBox='0 0 512 512' vertical-align='middle' aria-label='meeting target'>
                            <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                            <path fill='#ffffff' d='M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM369 209L241 337c-9.4 9.4-24.6 9.4-33.9 0l-64-64c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l47 47L335 175c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9z'></path>
                        </svg>
                        </div>
                    </div>
            ''',

    'monitoring':
                '''<div class="col-auto">
                        <div class="caption monitoring">
                            <svg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' height='36px' width='36px' vertical-align='middle' viewBox='0 0 512 512' aria-label='Measuring'>
                            <path fill='#fff' d='M256.5,512c141.4,0,256-114.6,256-256S397.9,0,256.5,0S0.5,114.6,0.5,256S115.1,512,256.5,512z'></path>
                            <path fill='#0f4d90' d='M217.6,149.2c0-16.1,13.1-29.1,29.1-29.1h19.4c16.1,0,29.1,13.1,29.1,29.1v213.7c0,16.1-13.1,29.1-29.1,29.1h-19.4c-16.1,0-29.1-13.1-29.1-29.1V149.2z M120.5,265.7c0-16.1,13.1-29.1,29.1-29.1h19.4c16.1,0,29.1,13.1,29.1,29.1v97.1c0,16.1-13.1,29.1-29.1,29.1h-19.4c-16.1,0-29.1-13.1-29.1-29.1V265.7z M343.9,158.9h19.4c16.1,0,29.1,13.1,29.1,29.1v174.8c0,16.1-13.1,29.1-29.1,29.1h-19.4c-16.1,0-29.1-13.1-29.1-29.1V188C314.8,171.9,327.8,158.9,343.9,158.9z'></path>
                            </svg>
                        </div>
                    </div>
                    ''',

    'near': 
                '''<div class="col-auto">
                        <div class="caption near">
                            <svg xmlns='http://www.w3.org/2000/svg' height='36px' width='36px' viewBox='0 0 512 512' vertical-align='middle'>
                            <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                            <path fill='#ffffff' d='M0 256a256 256 0 1 0 512 0A256 256 0 1 0 0 256zM297 385c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l71-71L120 280c-13.3 0-24-10.7-24-24s10.7-24 24-24l214.1 0-71-71c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0L409 239c9.4 9.4 9.4 24.6 0 33.9L297 385z' />
                            </svg>
                        </div>
                    </div>
                ''',
    'improve': 
                '''<div class="col-auto">
                        <div class="caption improve">
                            <svg xmlns='http://www.w3.org/2000/svg' height='36px' width='36px' viewBox='0 0 512 512' vertical-align='middle' aria-label='needs improvement icon'>
                            <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
                            <path fill='#ffffff' d='M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM175 175c9.4-9.4 24.6-9.4 33.9 0l47 47 47-47c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9l-47 47 47 47c9.4 9.4 9.4 24.6 0 33.9s-24.6 9.4-33.9 0l-47-47-47 47c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l47-47-47-47c-9.4-9.4-9.4-24.6 0-33.9z' />
                            </svg>
                        </div>
                    </div>
                '''
}

preamble = '''<style>

.section-body .row {
  margin-left: 0;
  margin-right: 0;
}

.margin-row a {
  display: flex;
  outline: none !important;
}

.col-lg-6 {
  position: relative;
  min-height: 1px;
  padding-right: 7px;
  padding-left: 7px;
}

  .card-h {
    position: relative;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-direction: column;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    margin: 7px 0;
    height: 170px;
    width: 100%;
  }
  /*.h-meeting{
    box-shadow:.25rem 0rem #58c04d!important;
  }
  .h-needs{
    box-shadow:.25rem 0rem #cc3000!important;
  }
  .h-near{
    box-shadow:.25rem 0rem #f99300!important;
  }
  .h-measuring{
    box-shadow:.25rem 0rem #2176d2!important;
  }*/
  .card-body{
    padding: 0 0px 0 20px;
    flex-grow: 1;
    display: flex;
    align-items: stretch;
    background-color: #f0f0f0;
    background-clip: border-box;
    border: 1px solid #a1a1a1;
    border-radius: .35rem;
  }
  
  .card-body:hover{
    background: #0f4d90;
    border: 2px solid #a1a1a1;
    cursor: pointer;
    transition: background 0.2s ease-in-out;
  }
  
  .card-body:hover .card-title,
  .card-body:hover .muted {
    color: #f0f0f0;
  }
  
  .card-body:hover .card-metric {
    color: #fff;
  }
  
  .card-row {
    display: flex;
    flex-wrap: wrap;
    height: 100%;
    width: 100%;
    min-height:150px;
  }
  .card-title {
    color:#666;
    font-weight:600;
    font-size: 1rem;
    font-family: var(--fontsHeadingFamily),Avenir Next;
    align-self: flex-start;
  }
  
  .card-title svg {
  display: none;
}

/* Show the svg only on mobile screens */
@media (max-width: 768px) {
  .card-title svg {
    display: inline-block;
    vertical-align: middle;
    fill: #444
  }
}
  
  .card-metric{
    font-weight: 600;
    color: #444;
    font-size:2.25rem;
    font-family: var(--fontsHeadingFamily),Avenir Next;
    align-self: center;
  }
  .muted {
    color: #666;
    font-family: var(--fontsBaseFamily),Avenir Next;
    font-size: 14px;
    align-self: flex-end;
    padding: 0 20px 0 0;
  }
  .col{
    flex-basis: 0;
    flex-grow: 1;
    max-width: 100%;
    display: grid;
  }
  .col-auto {
    flex: 0 0 auto;
    width: auto;
    max-width: none;
    align-content: center;
  }

  .metric-icon{
    /* box-shadow: 0 .5rem 1rem rgba(0,0,0,.15)!important;*/
  }
  .margin-row {
    margin-top: 10px;
  }
  
  .meets {
    background-color: #3a833c;
    padding: 10px;
    height:100%;
    border: 0px solid #3a833c;
    border-radius: 0 0.25rem 0.25rem 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .monitoring {
    background-color: #0f4d90;
    padding: 10px;
    text-align:-webkit-center;
    height:100%;
    border: 0px solid #0f4d90;
    border-radius: 0 0.25rem 0.25rem 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
    .near {
    background-color: #f99300;
    padding: 10px;
    height:100%;
    border: 0px solid #f99300;
    border-radius: 0 0.25rem 0.25rem 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
    .improve {
    background-color: #cc3000;
    padding: 10px;
    height:100%;
    border: 0px solid #cc3000;
    border-radius: 0 0.25rem 0.25rem 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .featured-gallery .caption {
    width: 100%;
    bottom: 0px;
    position: absolute;
    color: #444;
  }
  
  .card-body:hover .col-auto {
    background: white;
    border-radius: 0 0.25rem 0.25rem 0;
  }
  
  .card-body:hover .caption {
    opacity: 0.5;
    transition: opacity 0.1s ease-in-out;
  }
  
@media (max-width: 962px) {
  .margin-row {
    margin:0;
  }
}

@media (max-width: 550px) {
    .margin-row p {
    font-size: 10px;
  }
}

@media (max-width: 390px) {
    .margin-row {
    margin-top: 25px;
  }
}
  
</style>'''

safer_template = '''<div class="container-fluid">
  <div class="margin-row">
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <a href="/pages/homicides" aria-label="navigate to learn more about Philadelphia Homicides">
      <div class="card-h h-measuring card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">Number of Homicides&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{0}%</span>

              <p class="muted">Change in homicide count
              <br>
              (Compared to previous year)</p>
            </div>

            {1}

          </div>
        </div>
      </div>
      </a>
    </div>
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <a href="/pages/overdoses" aria-label="navigate to learn more about Fatal Overdoses in Philadelphia">
      <div class="card-h h-needs card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">Fatal Overdoses&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{2}*</span>

              <p class="muted" style="margin-bottom:0px;">Fatal overdoses in Philadelphia (2023*)</p>
              <p class="star">*preliminary</p>
            </div>

            {3}

          </div>
        </div>
      </div>
      </a>
    </div>
  </div>
  <div class="margin-row">
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <a href="/pages/911" aria-label="navigate to learn more about 9 1 1 Response Speed">
      <div class="card-h h-measuring card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">911 Call Center Response&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{4}%</span>

              <p class="muted">911 calls answered within 10 seconds
              <br>
              (Fiscal Year 2024, Q3)</p>
            </div>

           {5}

          </div>
        </div>
      </div>
      </a>
    </div>
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <a href="/pages/demolitions" aria-label="navigate to learn more about Dangerous Building Demolitions">
      <div class="card-h h-needs card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">Dangerous Building Demolitions&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{6}</span>

              <p class="muted">Dangerous buildings demolished
              <br>
              (August 2025)</p>
            </div>

            {7}

          </div>
        </div>
      </div>
      </a>
    </div>
  </div>
  <div class="margin-row">
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12">
     <a href="/pages/potholes" aria-label="Navigate to learn more about On Time Pothole Repairs">
      <div class="card-h h-near card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">On-Time Pothole Repairs&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{8}%</span>

              <p class="muted">Potholes repaired within 3 business days
              <br>
              (August 2025)</p>
            </div>
            
            {9}
          
          </div>
        </div>
      </div>
      </a>
    </div>
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <a href="/pages/traffic-calming" aria-label="navigate to learn more about Traffic Calming Measures">
      <div class="card-h h-needs card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">Speed Cushion Installations&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{10}</span>

              <p class="muted">Number of speed cushions installed
              <br>
              (August 2025)</p>
            </div>
            
            {11}
          
          </div>
        </div>
      </div>
      </a>
    </div>
  </div>
    <div class="margin-row">
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12">
     <a href="/pages/smoke-alarms" aria-label="navigate to learn more about Smoke Detector Installations">
      <div class="card-h h-near card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">Smoke Alarm Installations&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
             
               <span class="card-metric">{12}</span>

              <p class="muted">Number of Smoke Alarm Installed in Philadelphia
              <br>(January 2025)</p>
            </div>
            
            {13}
          
          </div>
        </div>
      </div>
      </a>
    </div>
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <a href="/pages/retail-thefts" aria-label="navigate to learn more about Retail Thefts in Philadelphia">
      <div class="card-h h-needs card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">Retail Thefts&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{14}</span>

              <p class="muted">Number of retail thefts
              <br>
              (August 2025)</p>
            </div>
            
            {15}
          
          </div>
        </div>
      </div>
      </a>
    </div>
  </div>
  <div class="margin-row">
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12" style="padding: 0 7px;">
      <a href="/pages/bee" aria-label="navigate to learn more about the bee program">
      <div class="card-h h-needs card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">BEE Investigations&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'>
              <path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{16}</span>

              <p class="muted">Number of Business Education and Enforcement (BEE) investigations conducted (Fiscal Year 2025, Q4)</p>
            </div>
            
            {17}

          </div>
        </div>
      </div>
      </a>
    </div>
    <div class="col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12" style="padding: 0 7px;">
      <a href="/pages/mental-health-first-aid" aria-label="navigate to learn more about mental health first aid">
      <div class="card-h h-needs card-stats">
        <div class="card-body">
          <div class="card-row">
            <div class="col">
              <h5 class="card-title">Mental Health First Aid&nbsp;
              <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 320 575' style='height: 16px;'>
              <path d='M310.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-192 192c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L242.7 256 73.4 86.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l192 192z' /></svg></h5>
              
              <span class="card-metric">{18}</span>

              <p class="muted">Number of individuals trained in Mental Health First Aid. (Fiscal Year 2025)</p>
            </div>
            
            {19}
          
          </div>
        </div>
      </div>
      </a>
    </div>
  </div>
</div>'''
