# OMF_BM_CHA

> omf_bm_cha

**Description:** Stores Connecticut Health Association benchmark data.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 63

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `HI_OUT_CNT` | DOUBLE |  |  | HI LOS outlier count |
| 5 | `HI_OUT_LOS` | DOUBLE |  |  | Average LOS for high LOS outliers |
| 6 | `HI_OUT_TOT_CHG` | DOUBLE |  |  | Average total charges for high LOS outliers |
| 7 | `IN_ANES_CHG` | DOUBLE |  |  | Inlier average anesthesia charges. |
| 8 | `IN_BED_CHG` | DOUBLE |  |  | Inlier average room charges |
| 9 | `IN_CHG1` | DOUBLE |  |  | Inlier average user defined charges1 |
| 10 | `IN_CHG10` | DOUBLE |  |  | Inlier average user defined charges10 |
| 11 | `IN_CHG2` | DOUBLE |  |  | Inlier average user defined charges2 |
| 12 | `IN_CHG3` | DOUBLE |  |  | Inlier average user defined charges3 |
| 13 | `IN_CHG4` | DOUBLE |  |  | Inlier average user defined charges4 |
| 14 | `IN_CHG5` | DOUBLE |  |  | Inlier average user defined charges5 |
| 15 | `IN_CHG6` | DOUBLE |  |  | Inlier average user defined charges6 |
| 16 | `IN_CHG7` | DOUBLE |  |  | Inlier average user defined charges7 |
| 17 | `IN_CHG8` | DOUBLE |  |  | Inlier average user defined charges8 |
| 18 | `IN_CHG9` | DOUBLE |  |  | Inlier average user defined charges9 |
| 19 | `IN_CHG_NBR_PATIENTS` | DOUBLE |  |  | Total inlier patients with charges. |
| 20 | `IN_CNT` | DOUBLE |  |  | Inlier count |
| 21 | `IN_ER_CHG` | DOUBLE |  |  | Inlier average emergency room charges |
| 22 | `IN_ICU_CCU_CHG` | DOUBLE |  |  | Inlier average ICU/CCU charges |
| 23 | `IN_ICU_LOS` | DOUBLE |  |  | Inlier ICU average length of stay. |
| 24 | `IN_LABOR_DELIV_CHG` | DOUBLE |  |  | Inlier average labor/delivery room charges |
| 25 | `IN_LAB_CHG` | DOUBLE |  |  | Inlier average laboratory charges |
| 26 | `IN_LAB_CHG_STDDEV` | DOUBLE |  |  | Inlier laboratory charges standard deviation |
| 27 | `IN_LOS` | DOUBLE |  |  | Inlier average LOS |
| 28 | `IN_LOS1` | DOUBLE |  |  | Inlier average user defined LOS1 |
| 29 | `IN_LOS2` | DOUBLE |  |  | Inlier average user defined LOS2 |
| 30 | `IN_LOS3` | DOUBLE |  |  | Inlier average user defined LOS3 |
| 31 | `IN_LOS4` | DOUBLE |  |  | Inlier average user defined LOS4 |
| 32 | `IN_LOS5` | DOUBLE |  |  | Inlier average user defined LOS5 |
| 33 | `IN_LOS_STDDEV` | DOUBLE |  |  | Inlier LOS standard deviation |
| 34 | `IN_MED_SURG_SUPP_CHG` | DOUBLE |  |  | Inlier average medical/surgical supply charges |
| 35 | `IN_MED_SURG_SUPP_CHG_STDDEV` | DOUBLE |  |  | Inlier medical/surgical supply charges standard deviation. |
| 36 | `IN_NBR_DEATHS` | DOUBLE |  |  | Total deaths for hospitals in the norms |
| 37 | `IN_NUCL_MED_CHG` | DOUBLE |  |  | Inlier average nuclear medicine charges. |
| 38 | `IN_NURSERY_CHG` | DOUBLE |  |  | Inlier average nursery charges |
| 39 | `IN_OR_CHG` | DOUBLE |  |  | Inlier average operating room charges. |
| 40 | `IN_OTHER_CHG` | DOUBLE |  |  | Inlier average all other charges |
| 41 | `IN_PHARM_CHG` | DOUBLE |  |  | Inlier average pharmacy charges |
| 42 | `IN_PHARM_CHG_STDDEV` | DOUBLE |  |  | Inlier pharmacy charges standard deviation. |
| 43 | `IN_PT_CHG` | DOUBLE |  |  | Inlier average physical therapy charges |
| 44 | `IN_RAD_CHG` | DOUBLE |  |  | Inlier average radiology charges. |
| 45 | `IN_RAD_CHG_STDDEV` | DOUBLE |  |  | Inlier radiology charges standard deviation |
| 46 | `IN_RECOV_CHG` | DOUBLE |  |  | Inlier average recovery room charges |
| 47 | `IN_RELATIVE_WEIGHT` | DOUBLE |  |  | Inlier relative weight |
| 48 | `IN_RESP_CHG` | DOUBLE |  |  | Inlier average respiratory services charges |
| 49 | `IN_ROM_NBR_PATIENTS` | DOUBLE |  |  | Total patients for hospitals in norms for risk of mortality subclass. |
| 50 | `IN_SOI_NBR_PATIENTS` | DOUBLE |  |  | Total patients for hospitals in norms for severity of illness subclass |
| 51 | `IN_TOT_CHG` | DOUBLE |  |  | Inlier average total charges |
| 52 | `IN_TOT_CHG_STDDEV` | DOUBLE |  |  | Inlier total charges standard deviation |
| 53 | `LOW_OUT_CNT` | DOUBLE |  |  | Los LOS outlier count |
| 54 | `LOW_OUT_LOS` | DOUBLE |  |  | Average LOS for low LOS outliers |
| 55 | `LOW_OUT_TOT_CHG` | DOUBLE |  |  | Average total charges for low LOS outliers |
| 56 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The nomenclature ID for the APRDRG code. |
| 57 | `OMF_BM_CHA_ID` | DOUBLE | NOT NULL |  | The unique identifier for the benchmark row. |
| 58 | `SUBCLASS_NBR` | DOUBLE |  |  | Subclass value (1 - Minor, 2 - Moderate, 3- Major, 4- Extreme) for Severity of Illness or Risk of Mortality. |
| 59 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 60 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 61 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 62 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 63 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

