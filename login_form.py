"""
Login form module for Resume Analyzer Application
"""
import streamlit as st
from streamlit_lottie import st_lottie
import requests

def render_login_form():
    """Render the login form that appears before the main application"""
    
    # Apply a custom style for the login form
    st.markdown("""
    <style>
    .login-container {
        max-width: 450px;
        margin: 0 auto;
        padding: 2rem;
        background: rgba(45, 45, 45, 0.9);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    .login-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .login-header h1 {
        color: white;
        font-size: 2rem;
        font-weight: 600;
    }
    
    .login-header p {
        color: #aaa;
        font-size: 1rem;
    }
    
    .input-container {
        margin-bottom: 1.5rem;
    }
    
    .input-field {
        width: 100%;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
        background: rgba(30, 30, 30, 0.9);
        color: white;
        transition: all 0.3s ease;
    }
    
    .login-button {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        border: none;
        font-weight: 500;
        cursor: pointer;
        width: 100%;
        text-align: center;
        margin-top: 1rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .login-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(76,175,80,0.3);
    }
    
    .signup-link {
        text-align: center;
        margin-top: 1.5rem;
        color: #aaa;
    }
    
    .signup-link a {
        color: #4CAF50;
        text-decoration: none;
        font-weight: 500;
    }
    
    .signup-link a:hover {
        text-decoration: underline;
    }
    
    .divider {
        display: flex;
        align-items: center;
        margin: 1.5rem 0;
        color: #aaa;
    }
    
    .divider::before, .divider::after {
        content: "";
        flex: 1;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    
    .divider span {
        padding: 0 1rem;
    }
    
    .social-login {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .social-icon {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: rgba(30, 30, 30, 0.9);
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255,255,255,0.1);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .social-icon:hover {
        transform: translateY(-3px);
        background: rgba(40, 40, 40, 0.9);
        border-color: #4CAF50;
    }
    
    .forgot-password {
        text-align: right;
        margin-top: 0.5rem;
    }
    
    .forgot-password a {
        color: #4CAF50;
        text-decoration: none;
        font-size: 0.9rem;
    }
    
    .forgot-password a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)
    
    def load_lottie_url(url: str):
        """Load Lottie animation from URL"""
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    # Center everything on screen
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Lottie animation for the login page
        lottie_login = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_nc1bp7st.json")
        st_lottie(lottie_login, height=200, key="login_animation")
        
        # Login container
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # Login header
        st.markdown("""
            <div class="login-header">
                <h1>Welcome to Resume Analyzer</h1>
                <p>Enter your credentials to access your account</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Login form
        email = st.text_input("Email", placeholder="Enter your email", key="login_email")
        
        # Password field with "Forgot Password" link
        password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")
        
        st.markdown("""
            <div class="forgot-password">
                <a href="#">Forgot Password?</a>
            </div>
        """, unsafe_allow_html=True)
        
        # Login button
        login_button = st.button("Login", key="login_submit", type="primary")
        
        # Divider
        st.markdown("""
            <div class="divider">
                <span>OR</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Social login
        st.markdown("""
            <div class="social-login">
                <div class="social-icon">
                    <i class="fab fa-google" style="color: #DB4437;"></i>
                </div>
                <div class="social-icon">
                    <i class="fab fa-facebook-f" style="color: #4267B2;"></i>
                </div>
                <div class="social-icon">
                    <i class="fab fa-twitter" style="color: #1DA1F2;"></i>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Sign up link
        st.markdown("""
            <div class="signup-link">
                Don't have an account? <a href="#">Sign Up</a>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Handle login logic
        if login_button:
            if email and password:  # Simple validation
                # For demo purposes, any non-empty input will work
                st.session_state.is_logged_in = True
                st.session_state.current_user_email = email
                st.rerun()
            else:
                st.error("Please enter both email and password")