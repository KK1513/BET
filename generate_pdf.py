#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
皇冠娛樂城專案說明 PDF 生成器
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
import os
from datetime import datetime

def create_pdf():
    """創建 PDF 簡報"""
    
    # 創建 PDF 文檔
    filename = "皇冠娛樂城專案說明簡報.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # 獲取樣式
    styles = getSampleStyleSheet()
    
    # 創建自定義樣式
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#FFD700'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#2d1b69'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#1a0033'),
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        spaceAfter=5,
        leftIndent=20,
        fontName='Helvetica'
    )
    
    # 構建內容
    story = []
    
    # 封面
    story.append(Spacer(1, 5*cm))
    story.append(Paragraph("皇冠娛樂城", title_style))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("線上娛樂平台專案說明簡報", title_style))
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph(f"生成日期：{datetime.now().strftime('%Y年%m月%d日')}", normal_style))
    story.append(PageBreak())
    
    # 目錄
    story.append(Paragraph("目錄", heading_style))
    story.append(Spacer(1, 1*cm))
    
    toc_items = [
        "1. 專案概述",
        "2. 系統架構",
        "3. 核心功能模組",
        "4. 技術架構",
        "5. 用戶端功能",
        "6. 管理後台功能",
        "7. 遊戲分類",
        "8. 設計特色",
        "9. 技術特點",
        "10. 未來發展"
    ]
    
    for item in toc_items:
        story.append(Paragraph(f"• {item}", bullet_style))
    
    story.append(PageBreak())
    
    # 1. 專案概述
    story.append(Paragraph("1. 專案概述", heading_style))
    story.append(Paragraph(
        "皇冠娛樂城是一個功能完整的線上娛樂平台系統，提供多種遊戲類別和完整的用戶管理、交易管理功能。"
        "系統採用響應式設計，支援桌面端和手機端訪問，提供流暢的用戶體驗。",
        normal_style
    ))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("專案目標", subheading_style))
    story.append(Paragraph("• 提供安全、便捷的線上娛樂平台", bullet_style))
    story.append(Paragraph("• 支援多種遊戲類別和支付方式", bullet_style))
    story.append(Paragraph("• 實現完整的用戶管理系統", bullet_style))
    story.append(Paragraph("• 提供強大的管理後台功能", bullet_style))
    story.append(Paragraph("• 優化移動端用戶體驗", bullet_style))
    story.append(PageBreak())
    
    # 2. 系統架構
    story.append(Paragraph("2. 系統架構", heading_style))
    story.append(Paragraph("系統採用前端單頁應用架構，主要包含以下部分：", normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("2.1 前端結構", subheading_style))
    frontend_data = [
        ['模組', '說明'],
        ['index.html', '主頁面，包含用戶登入、註冊、遊戲大廳等功能'],
        ['admin.html', '管理後台，提供用戶管理、交易管理等功能'],
        ['遊戲分類頁面', 'live.html, sports.html, slots.html 等遊戲專屬頁面'],
        ['common.css', '共用樣式表，定義統一的視覺風格'],
        ['common.js', '共用 JavaScript 函數庫']
    ]
    
    frontend_table = Table(frontend_data, colWidths=[5*cm, 11*cm])
    frontend_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2d1b69')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(frontend_table)
    story.append(PageBreak())
    
    # 3. 核心功能模組
    story.append(Paragraph("3. 核心功能模組", heading_style))
    
    story.append(Paragraph("3.1 用戶管理模組", subheading_style))
    story.append(Paragraph("• 用戶註冊：支援帳號、密碼、手機、Email 註冊", bullet_style))
    story.append(Paragraph("• 用戶登入：安全的登入驗證機制", bullet_style))
    story.append(Paragraph("• 個人資料管理：查看和修改個人資訊", bullet_style))
    story.append(Paragraph("• 密碼修改：安全的密碼更換功能", bullet_style))
    story.append(Paragraph("• VIP 等級系統：根據投注累積自動升級", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("3.2 交易管理模組", subheading_style))
    story.append(Paragraph("• 充值功能：支援銀行轉帳、支付寶、微信支付", bullet_style))
    story.append(Paragraph("• 提款功能：安全的提款申請和審核流程", bullet_style))
    story.append(Paragraph("• 交易記錄：完整的交易歷史查詢", bullet_style))
    story.append(Paragraph("• 餘額管理：即時餘額顯示和更新", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("3.3 遊戲模組", subheading_style))
    story.append(Paragraph("• 遊戲分類：8 大遊戲類別，滿足不同玩家需求", bullet_style))
    story.append(Paragraph("• 遊戲過濾：智能分類和搜索功能", bullet_style))
    story.append(Paragraph("• 遊戲入口：一鍵進入各種遊戲", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("3.4 活動模組", subheading_style))
    story.append(Paragraph("• 每日簽到：每日登入領取獎勵", bullet_style))
    story.append(Paragraph("• 優惠活動：首儲優惠、返水、推薦好友等", bullet_style))
    story.append(Paragraph("• 促銷跑馬燈：即時顯示最新優惠資訊", bullet_style))
    story.append(PageBreak())
    
    # 4. 技術架構
    story.append(Paragraph("4. 技術架構", heading_style))
    
    story.append(Paragraph("4.1 前端技術", subheading_style))
    tech_data = [
        ['技術', '版本/說明', '用途'],
        ['HTML5', '最新標準', '頁面結構'],
        ['CSS3', '最新標準', '樣式和動畫效果'],
        ['JavaScript (ES6+)', '原生 JS', '交互邏輯和功能實現'],
        ['Bootstrap', '5.3.0', '響應式框架和 UI 組件'],
        ['Font Awesome', '6.4.0', '圖標庫'],
        ['LocalStorage', 'Web API', '本地數據存儲']
    ]
    
    tech_table = Table(tech_data, colWidths=[4*cm, 5*cm, 7*cm])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FFD700')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(tech_table)
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("4.2 數據存儲", subheading_style))
    story.append(Paragraph(
        "系統使用瀏覽器的 LocalStorage API 進行數據存儲，包括：",
        normal_style
    ))
    story.append(Paragraph("• 用戶數據（users）：存儲所有註冊用戶資訊", bullet_style))
    story.append(Paragraph("• 交易記錄（transactions）：存儲所有交易明細", bullet_style))
    story.append(Paragraph("• 管理員帳號（adminAccounts）：存儲後台管理員資訊", bullet_style))
    story.append(Paragraph("• 當前用戶（currentUser）：存儲當前登入用戶狀態", bullet_style))
    story.append(PageBreak())
    
    # 5. 用戶端功能
    story.append(Paragraph("5. 用戶端功能", heading_style))
    
    story.append(Paragraph("5.1 主頁功能", subheading_style))
    story.append(Paragraph("• 響應式設計：自動適配桌面和手機螢幕", bullet_style))
    story.append(Paragraph("• 動態背景：視覺效果豐富的動畫背景", bullet_style))
    story.append(Paragraph("• 遊戲大廳：8 大遊戲分類卡片展示", bullet_style))
    story.append(Paragraph("• 優惠活動：展示最新優惠和促銷資訊", bullet_style))
    story.append(Paragraph("• 跑馬燈公告：即時顯示重要訊息", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("5.2 手機端特色", subheading_style))
    story.append(Paragraph("• 左側垂直導航：快速切換遊戲分類", bullet_style))
    story.append(Paragraph("• 底部導航欄：優惠、帳務、存提、服務、個人中心", bullet_style))
    story.append(Paragraph("• 浮動簽到按鈕：便捷的每日簽到入口", bullet_style))
    story.append(Paragraph("• 2x3 遊戲網格：優化的遊戲卡片布局", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("5.3 用戶功能", subheading_style))
    user_features = [
        ['功能', '說明'],
        ['註冊/登入', '完整的用戶註冊和登入系統'],
        ['充值', '支援多種支付方式，最低 100 元'],
        ['提款', '安全的提款申請，1-3 個工作天處理'],
        ['交易查詢', '完整的交易記錄，支援分類篩選'],
        ['每日簽到', '每日登入領取 50-150 元隨機獎勵'],
        ['個人中心', '查看個人資料、修改密碼等功能'],
        ['客服服務', '電話、WhatsApp、Telegram 多管道客服']
    ]
    
    user_table = Table(user_features, colWidths=[5*cm, 11*cm])
    user_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2d1b69')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    story.append(user_table)
    story.append(PageBreak())
    
    # 6. 管理後台功能
    story.append(Paragraph("6. 管理後台功能", heading_style))
    
    story.append(Paragraph("6.1 登入系統", subheading_style))
    story.append(Paragraph("• 管理員帳號認證：預設帳號 admin/admin123", bullet_style))
    story.append(Paragraph("• 登入狀態保持：自動記住登入狀態", bullet_style))
    story.append(Paragraph("• 安全登出：登出時清除登入資訊", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("6.2 儀表板", subheading_style))
    story.append(Paragraph("• 總用戶數：統計所有註冊用戶", bullet_style))
    story.append(Paragraph("• 總餘額：所有用戶的總餘額", bullet_style))
    story.append(Paragraph("• 總交易數：系統所有交易記錄數量", bullet_style))
    story.append(Paragraph("• 總充值：累計充值金額統計", bullet_style))
    story.append(Paragraph("• 總提款：累計提款金額統計", bullet_style))
    story.append(Paragraph("• 今日新增用戶：當天註冊的用戶數量", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("6.3 用戶管理", subheading_style))
    story.append(Paragraph("• 用戶列表：顯示所有註冊用戶資訊", bullet_style))
    story.append(Paragraph("• 用戶搜索：支援帳號、手機、Email 搜索", bullet_style))
    story.append(Paragraph("• 編輯用戶：修改用戶資訊（開發中）", bullet_style))
    story.append(Paragraph("• 調整餘額：管理員可手動調整用戶餘額", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("6.4 交易管理", subheading_style))
    story.append(Paragraph("• 交易列表：顯示所有交易記錄", bullet_style))
    story.append(Paragraph("• 交易篩選：按類型篩選（全部、充值、提款、投注、中獎）", bullet_style))
    story.append(Paragraph("• 交易搜索：按用戶名和類型搜索", bullet_style))
    story.append(Paragraph("• 提款審核：審核通過待處理的提款申請", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("6.5 其他功能", subheading_style))
    story.append(Paragraph("• 遊戲管理：遊戲類別管理（開發中）", bullet_style))
    story.append(Paragraph("• 優惠管理：優惠活動管理（開發中）", bullet_style))
    story.append(Paragraph("• 報表統計：數據統計和分析（開發中）", bullet_style))
    story.append(PageBreak())
    
    # 7. 遊戲分類
    story.append(Paragraph("7. 遊戲分類", heading_style))
    
    games_data = [
        ['遊戲類別', '頁面', '遊戲內容'],
        ['真人視訊', 'live.html', '美女荷官、百家樂、龍虎、輪盤'],
        ['體育競技', 'sports.html', '足球、籃球、電競、賽事直播'],
        ['棋牌遊戲', 'chess.html', '德州撲克、麻將、鬥地主'],
        ['電子遊藝', 'slots.html', '老虎機、水果機、爆分機台'],
        ['彩票投注', 'lottery.html', '時時彩、快3、北京賽車'],
        ['捕魚機台', 'fishing.html', '千炮捕魚、深海狩獵、高倍獎金'],
        ['娛樂直播', 'streaming.html', '美女主播、互動遊戲、送禮'],
        ['電競賽事', 'esports.html', 'LOL、DOTA2、CS:GO 投注'],
        ['Bet365', 'bet365.html', 'Bet365 體育投注平台']
    ]
    
    games_table = Table(games_data, colWidths=[4*cm, 4*cm, 8*cm])
    games_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FFD700')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.beige]),
    ]))
    story.append(games_table)
    story.append(PageBreak())
    
    # 8. 設計特色
    story.append(Paragraph("8. 設計特色", heading_style))
    
    story.append(Paragraph("8.1 視覺設計", subheading_style))
    story.append(Paragraph("• 主題色彩：金色（#FFD700）搭配深紫色（#1a0033），營造高貴奢華感", bullet_style))
    story.append(Paragraph("• 漸變效果：大量使用漸變背景，增強視覺層次", bullet_style))
    story.append(Paragraph("• 動畫效果：浮動背景、按鈕動畫、卡片懸停效果", bullet_style))
    story.append(Paragraph("• 響應式設計：完美適配桌面和手機端", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("8.2 用戶體驗", subheading_style))
    story.append(Paragraph("• 直觀導航：清晰的導航結構，易於使用", bullet_style))
    story.append(Paragraph("• 即時反饋：Toast 通知、加載動畫等即時狀態提示", bullet_style))
    story.append(Paragraph("• 快速操作：一鍵登入、快速充值、便捷簽到", bullet_style))
    story.append(Paragraph("• 數據驗證：完整的表單驗證和錯誤提示", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("8.3 功能完整性", subheading_style))
    story.append(Paragraph("• 完整的用戶生命週期管理", bullet_style))
    story.append(Paragraph("• 完整的交易流程管理", bullet_style))
    story.append(Paragraph("• 完整的後台管理系統", bullet_style))
    story.append(Paragraph("• 豐富的遊戲分類和入口", bullet_style))
    story.append(PageBreak())
    
    # 9. 技術特點
    story.append(Paragraph("9. 技術特點", heading_style))
    
    story.append(Paragraph("9.1 前端技術亮點", subheading_style))
    story.append(Paragraph("• 純前端實現：無需後端伺服器，使用 LocalStorage 存儲", bullet_style))
    story.append(Paragraph("• 模組化設計：共用 CSS 和 JS 文件，便於維護", bullet_style))
    story.append(Paragraph("• 響應式布局：使用 Bootstrap 實現完美適配", bullet_style))
    story.append(Paragraph("• 動態交互：豐富的 JavaScript 交互效果", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("9.2 數據管理", subheading_style))
    story.append(Paragraph("• LocalStorage 存儲：使用瀏覽器本地存儲", bullet_style))
    story.append(Paragraph("• 數據結構化：統一的數據格式和命名規範", bullet_style))
    story.append(Paragraph("• 狀態管理：統一的用戶狀態管理機制", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("9.3 安全性", subheading_style))
    story.append(Paragraph("• 表單驗證：前端的輸入驗證機制", bullet_style))
    story.append(Paragraph("• 密碼保護：密碼存儲和驗證（實際應用需加密）", bullet_style))
    story.append(Paragraph("• 登入狀態：安全的登入狀態管理", bullet_style))
    story.append(PageBreak())
    
    # 10. 未來發展
    story.append(Paragraph("10. 未來發展", heading_style))
    
    story.append(Paragraph("10.1 功能擴展", subheading_style))
    story.append(Paragraph("• 後端 API 整合：連接真實的後端服務", bullet_style))
    story.append(Paragraph("• 數據庫整合：使用 MySQL/PostgreSQL 存儲數據", bullet_style))
    story.append(Paragraph("• 支付系統整合：連接真實的支付閘道", bullet_style))
    story.append(Paragraph("• 遊戲平台整合：接入真實的遊戲供應商", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("10.2 技術升級", subheading_style))
    story.append(Paragraph("• 框架升級：考慮使用 React/Vue 等現代框架", bullet_style))
    story.append(Paragraph("• 狀態管理：使用 Redux/Vuex 等狀態管理工具", bullet_style))
    story.append(Paragraph("• 構建工具：使用 Webpack/Vite 等構建工具", bullet_style))
    story.append(Paragraph("• 測試框架：添加單元測試和 E2E 測試", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("10.3 功能完善", subheading_style))
    story.append(Paragraph("• 遊戲管理：完整的遊戲類別和內容管理", bullet_style))
    story.append(Paragraph("• 優惠管理：靈活的優惠活動配置系統", bullet_style))
    story.append(Paragraph("• 報表統計：詳細的數據分析和報表生成", bullet_style))
    story.append(Paragraph("• 消息系統：站內消息和通知系統", bullet_style))
    story.append(Paragraph("• 多語言支援：國際化功能", bullet_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph("10.4 性能優化", subheading_style))
    story.append(Paragraph("• 代碼分割：按需加載，減少初始載入時間", bullet_style))
    story.append(Paragraph("• 圖片優化：使用 WebP 格式和懶加載", bullet_style))
    story.append(Paragraph("• 緩存策略：合理的緩存機制", bullet_style))
    story.append(Paragraph("• CDN 加速：使用 CDN 加速靜態資源", bullet_style))
    story.append(PageBreak())
    
    # 總結
    story.append(Paragraph("總結", heading_style))
    story.append(Paragraph(
        "皇冠娛樂城是一個功能完整、設計精美的線上娛樂平台系統。系統採用現代化的前端技術，"
        "提供完整的用戶端和管理端功能，支援多種遊戲類別，具有良好的用戶體驗和擴展性。"
        "系統架構清晰，代碼結構良好，為後續的功能擴展和技術升級奠定了良好的基礎。",
        normal_style
    ))
    story.append(Spacer(1, 1*cm))
    
    story.append(Paragraph(
        f"本簡報生成時間：{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}",
        ParagraphStyle(
            'CustomFooter',
            parent=styles['Normal'],
            fontSize=9,
            textColor=colors.grey,
            alignment=TA_CENTER
        )
    ))
    
    # 構建 PDF
    doc.build(story)
    print(f"PDF 簡報已生成：{filename}")
    print(f"文件位置：{os.path.abspath(filename)}")

if __name__ == "__main__":
    try:
        create_pdf()
    except Exception as e:
        print(f"生成 PDF 時發生錯誤：{e}")
        print("請確保已安裝 reportlab 庫：pip install reportlab")


