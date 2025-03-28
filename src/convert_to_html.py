import nbconvert
import os
import subprocess

def convert_notebook_to_html():
    # Đường dẫn đến notebook
    notebook_path = 'ipynb2pdf.ipynb'
    
    # Đường dẫn output HTML
    output_path = 'docs/report.html'
    
    # Đảm bảo thư mục docs tồn tại
    os.makedirs('docs', exist_ok=True)
    
    # Chuyển đổi từ .ipynb sang .html
    try:
        # Chuyển đổi sang HTML
        subprocess.run([
            'jupyter', 'nbconvert',
            '--to', 'html',
            '--output', output_path,
            notebook_path
        ], check=True)
        print(f"Đã chuyển đổi thành công: {output_path}")
        print("\nBạn có thể mở file HTML và in sang PDF bằng trình duyệt web")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chuyển đổi: {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")

if __name__ == '__main__':
    convert_notebook_to_html() 