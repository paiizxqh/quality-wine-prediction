import React, { useEffect } from "react";
import "antd/dist/reset.css";
import { Layout } from "antd";
import Prediction from "./components/Prediction";
import '../src/css/style.css';
import paperTexture from './assets/images/vintage-paper-texture.jpg';
import grapeVineLeft from './assets/images/grape-vine-left.png';
import grapeVineRight from './assets/images/grape-vine-right.png';

const { Header, Content, Footer } = Layout;

const App: React.FC = () => {
  useEffect(() => {
    // Parallax effect
    const handleScroll = () => {
      const scrolled = window.pageYOffset;
      const parallaxElements = document.querySelectorAll('.parallax');
      parallaxElements.forEach((element) => {
        const el = element as HTMLElement;
        const speed = el.dataset.speed || '0.5';
        el.style.transform = `translateY(${scrolled * parseFloat(speed)}px)`;
      });
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <Layout className="vintage-layout" style={{ 
        backgroundImage: `url(${paperTexture})`, 
        backgroundSize: 'cover', 
        backgroundRepeat: 'no-repeat' 
    }}>
      <div className="vintage-decorations">
        <img 
          src={grapeVineLeft} 
          alt="Grape Vine Left" 
          className="decoration left parallax" 
          data-speed="0.3" 
        />
        <img 
          src={grapeVineRight} 
          alt="Grape Vine Right" 
          className="decoration right parallax" 
          data-speed="0.3" 
        />
      </div>
      <Header className="vintage-header">
        <div className="header-content">
          <span className="header-decoration">🍷</span>
          Wine Quality Prediction
          <span className="header-decoration">🍷</span>
        </div>
      </Header>
      <Content className="vintage-content">
        <div className="content-wrapper">
          <Prediction />
        </div>
      </Content>
      <Footer className="vintage-footer">
        <div className="footer-content">
          Wine Quality Prediction ©2024 Created by Group 11 (Malc Super Pai)
        </div>
      </Footer>
    </Layout>
  );
};

export default App;