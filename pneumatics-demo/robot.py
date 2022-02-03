#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        self.solenoid = wpilib.DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM,2,3)
        

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot
    def teleopInit(self):
        pass
        # self.solenoid.set(self.solenoid.Value.kReverse)
    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())

        if self.stick.getRawButtonPressed(3):
            # if self.solenoid.get() == self.solenoid.Value.kForward:
            #     self.solenoid.set(self.solenoid.Value.kReverse)
            # elif self.solenoid.get() == self.solenoid.Value.kReverse:
            #     self.solenoid.set(self.solenoid.Value.kForward)
            # self.solenoid.set(self.solenoid.get)
            self.solenoid.toggle()
            if self.solenoid.get() == self.solenoid.Value.kOff:
                self.solenoid.set(self.solenoid.Value.kForward)
            # self.solenoid.set(wpilib.DoubleSolenoid.Value.kForward)
            print("worked")
            
        


if __name__ == "__main__":
    wpilib.run(MyRobot)