import prob_loader as loader
import vrp_modules as vrp
import google_solver as google
import disp_rule as dr


def main():
    # Bad Sungbum
    new_instance = loader.load_prob_xlsx('VRPProb_TW.xlsx')
    solution1 = dr.solve_dr_vi(new_instance)
    solution2 = dr.solve_dr_ti(new_instance)
    print("End of Program")


if __name__ == '__main__':
    main()
