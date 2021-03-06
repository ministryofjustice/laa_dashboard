def globals(request):

    return {
        'app_title': 'LAA Service Status', # Application Title (Populates <title>)
        'proposition_title': 'LAA Service Status', # Proposition Title (Populates proposition header)
        'phase': 'alpha', # Current Phase (Sets the current phase and the colour of phase tags). Presumed values: alpha, beta, live
        'product_type': 'service', # Product Type (Adds class to body based on service type). Presumed values: information, service
        'feedback_url': 'test.test.test', # Feedback URL (URL for feedback link in phase banner)
    }

# 'app_title' does not seem to passed to the template?
