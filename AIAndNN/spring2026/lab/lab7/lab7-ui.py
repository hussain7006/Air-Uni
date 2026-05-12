import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import time
import threading

# Global styling
ctk.set_appearance_mode("Dark")


class KNNLiveDispersedEngine(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Air University | KNN Live Scattered Visualizer")
        self.geometry("1200x800")

        # Colors
        self.neon_blue = "#6366f1"
        self.play_green = "#10b981"
        self.stay_red = "#f43f5e"

        # Data setup
        self.setup_engine()

        # UI Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self, width=300, fg_color="#111827", corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Line 42 (Font Error Fix)
        self.logo = ctk.CTkLabel(self.sidebar, text="KNN SCATTER ENGINE", font=(
            "Arial", 18, "bold"), text_color=self.neon_blue)
        self.logo.pack(pady=30)

        # Controls
        self.k_label = ctk.CTkLabel(
            self.sidebar, text="Hyperparameter K:", font=("Plus Jakarta Sans", 12))
        self.k_label.pack(pady=(20, 0))
        self.k_slider = ctk.CTkSlider(
            self.sidebar, from_=1, to=9, number_of_steps=4, button_color=self.neon_blue)
        self.k_slider.set(3)
        # Line 48 (Fix: padx instead of px)
        self.k_slider.pack(pady=10, padx=20)

        self.btn_run = ctk.CTkButton(self.sidebar, text="START LIVE SCAN", font=("Plus Jakarta Sans", 13, "bold"),
                                     fg_color=self.neon_blue, hover_color="#4338ca", height=45, command=self.start_live_process)
        self.btn_run.pack(pady=30, padx=20, fill="x")

        # Live Terminal
        self.terminal = ctk.CTkTextbox(self.sidebar, height=200, fg_color="#000", font=(
            "Consolas", 11), text_color="#10b981")
        self.terminal.pack(pady=10, padx=15, fill="x")
        self.log("System Ready. Waiting for input...")

        # Result Card
        self.res_card = ctk.CTkFrame(
            self.sidebar, fg_color="#1f2937", height=100)
        self.res_card.pack(pady=20, padx=15, fill="x")
        self.res_txt = ctk.CTkLabel(
            self.res_card, text="---", font=("Impact", 24))
        self.res_txt.place(relx=0.5, rely=0.5, anchor="center")

        # Graph Area
        self.main_viz = ctk.CTkFrame(
            self, fg_color="#030712", corner_radius=20)
        self.main_viz.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.fig, self.ax = plt.subplots(figsize=(8, 6), facecolor="#030712")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_viz)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=20)

        self.initial_draw()

    def setup_engine(self):
        # Weather: 0:Overcast, 1:Rainy, 2:Sunny | Temp: 0:Cool, 1:Hot, 2:Mild
        self.features = np.array([[2, 1], [2, 1], [0, 1], [1, 2], [1, 0], [1, 0], [
                                 0, 0], [2, 2], [2, 0], [1, 2], [2, 2], [0, 2], [0, 1], [1, 2]])
        self.labels = np.array(
            [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])  # 1: Play, 0: No

        # Add random scattering to points to make them dispersed
        # Weather is x, Temp is y
        scatter_range = 0.15  # points will scatter by max 0.15 around original coordinate
        self.scattered_features = self.features.astype(
            float) + np.random.uniform(-scatter_range, scatter_range, self.features.shape)

    def log(self, msg):
        self.terminal.insert("end", f"> {msg}\n")
        self.terminal.see("end")

    def initial_draw(self):
        self.ax.clear()
        self.ax.set_facecolor("#030712")
        self.ax.grid(True, color="#1e293b", alpha=0.3)

        # Plot dispersed existing points with glow
        for i, pt in enumerate(self.scattered_features):
            color = self.play_green if self.labels[i] == 1 else self.stay_red
            self.ax.scatter(pt[0], pt[1], color=color, s=150,
                            edgecolors='white', alpha=0.8, zorder=3)
            self.ax.scatter(pt[0], pt[1], color=color,
                            s=400, alpha=0.1, zorder=2)

        # Draw central decision boundary markers (just for reference)
        for x in range(3):
            for y in range(3):
                self.ax.scatter(x, y, color='white', s=10, alpha=0.1, zorder=1)

        self.ax.set_xticks([0, 1, 2])
        self.ax.set_yticks([0, 1, 2])
        self.ax.set_xticklabels(["Overcast", "Rainy", "Sunny"], color="gray")
        self.ax.set_yticklabels(["Cool", "Hot", "Mild"], color="gray")
        # ensure points near boundaries are visible
        self.ax.set_xlim(-0.5, 2.5)
        self.ax.set_ylim(-0.5, 2.5)
        self.canvas.draw()

    def start_live_process(self):
        # Running in a thread so UI doesn't freeze
        threading.Thread(target=self.live_logic, daemon=True).start()

    def live_logic(self):
        self.log("Initializing Scattered Training Phase...")
        self.res_txt.configure(text="TRAINING...", text_color="yellow")
        time.sleep(1)

        # Simulation: Scanning data
        for i in range(5):
            self.log(f"Mapping Feature Space... {20*(i+1)}%")
            time.sleep(0.3)

        # Pick a query (Let's say Weather: Sunny(2), Temp: Mild(2))
        query = np.array([2, 2])
        self.log(f"Predicting for: Sunny & Mild")

        # Plot Query with animation
        self.ax.scatter(query[0], query[1], color='white',
                        marker='s', s=300, zorder=5, label="Target")
        self.canvas.draw()

        self.log("Calculating Euclidean Distances to all scattered points...")
        time.sleep(1)

        # KNN Computation
        k = int(self.k_slider.get())
        if k % 2 == 0:
            k += 1

        knn = KNeighborsClassifier(n_neighbors=k)
        # Use scattered features for training
        knn.fit(self.scattered_features, self.labels)

        distances, indices = knn.kneighbors([query])

        # Show Radar Lines one by one
        for idx in indices[0]:
            # Use scattered point as target
            target_pt = self.scattered_features[idx]
            self.ax.plot([query[0], target_pt[0]], [query[1], target_pt[1]],
                         color=self.neon_blue, linewidth=2, linestyle='--', alpha=0.8)
            self.log(
                f"Neighbor Found! Dispersed Distance: {np.linalg.norm(query-target_pt):.2f}")
            self.canvas.draw()
            time.sleep(0.6)

        # Final Vote
        prediction = knn.predict([query])[0]
        result = "PLAY" if prediction == 1 else "NO PLAY"
        color = self.play_green if prediction == 1 else self.stay_red

        self.log(f"Voting Complete: Majority is {result}")
        self.res_txt.configure(text=result, text_color=color)

        # Visual Glow for Query
        self.ax.scatter(query[0], query[1], color=color,
                        s=800, alpha=0.2, zorder=1)
        self.canvas.draw()


if __name__ == "__main__":
    app = KNNLiveDispersedEngine()
    app.mainloop()
