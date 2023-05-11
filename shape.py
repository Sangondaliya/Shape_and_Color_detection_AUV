

'''
def detect(self, contour, debug):
        shape = "undefined"
        epsilon = 0.03 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(self.img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv.rectangle(self.img, (x, y-10), (x + w, y + 10), (0, 0, 255), -1)
        font = cv.FONT_HERSHEY_SIMPLEX
        number = ""
        if debug:
            cv.drawContours(self.img, [contour], 0, (0, 255, 0), 2)

            for pt in approx:
                cv.circle(self.img, (pt[0][0], pt[0][1]), 5, (255, 0, 0), -1)
            number = str(len(approx)) + " "
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            # print(w, h, w / h)
            if 0.95 < w / h < 1.05:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif len(approx) == 5:
            shape = "Pentagon"
        else:
            shape = "Circle"
        cv.putText(self.img, number + shape, (x, y), font, 0.4, (255, 255, 255), 1, cv.LINE_AA)
'''