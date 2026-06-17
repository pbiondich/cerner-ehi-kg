# PFT_RVU_CONTENT

> Stores information from the CMS National Physician Fee Schedule Relative Value Filegeographical location of practice to determine how much providers can charge for Medicare-reimbursed services.

**Description:** Profit Relative Value Unit Content  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSISTANT_AT_SURGERY_CD` | DOUBLE | NOT NULL |  | Indicates services where an assistant at surgery is never paid for per Medicare claims manual. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `BILATERAL_SURGERY_CD` | DOUBLE | NOT NULL |  | Indicates services subject to payment adjustment. |
| 5 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related billing entity |
| 6 | `CDM_VALUE_TXT` | VARCHAR(50) |  |  | Contains the text value of the charge master description. |
| 7 | `CDM_VALUE_TXT_KEY` | VARCHAR(50) |  |  | Contains the text value of the charge master description in all capitals and with no special characters. |
| 8 | `CONVERSION_FACTOR_NBR` | DOUBLE |  |  | Multiplier that transforms relative values into payment amounts. |
| 9 | `COSURGEONS_CD` | DOUBLE | NOT NULL |  | Indicates services for which two surgeons, each in a different specialty, may be paid. |
| 10 | `ENDOSCOPIC_BASE_CODE_TXT` | VARCHAR(5) |  |  | Code which identifies an endoscopic base code for each code with a multiple surgery indicator of 3 |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `FACILITY_NA_IND` | DOUBLE |  |  | Indicates whether or not the procedure is rarely or never performed in the facility setting |
| 13 | `FACILITY_PRACTICE_EXP_RVU_NBR` | DOUBLE |  |  | RVU for fully-implemented resource based practice expense for the facility setting |
| 14 | `GLOBAL_SURGERY_CD` | DOUBLE | NOT NULL |  | Provides time frames that apply to each surgical procedure. |
| 15 | `INTRAOPERATIVE_PCT` | DOUBLE |  |  | Percentage for intraoperative portion of global package, including postoperative work in the hospital |
| 16 | `MALPRACTICE_RVU_NBR` | DOUBLE |  |  | RVU for the malpractice expense for the service |
| 17 | `MEDICARE_PYMT_PURPOSE_IND` | DOUBLE |  |  | Indicates whether or not RVU are used for Medicare payment purposes |
| 18 | `MOD_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Identifies nomenclature for HCPCS or CPT4 modifier code |
| 19 | `MOD_TXT` | VARCHAR(200) |  |  | Contains the Identifier of the Modifiers for CPT and HCPCS. When new nomenclature content is loaded in the middle of the year, nomenclature ids don¿t match for the same source identifiers, so instead of qualifying on nomenclature ids in Revenue GSR we want to qualify on Source Identifier itself. |
| 20 | `MULTIPLE_PROCEDURE_CD` | DOUBLE | NOT NULL |  | Provides applicable payment adjustment rule for multiple procedures. |
| 21 | `NON_FAC_NA_IND` | DOUBLE |  |  | Indicates whether or not the procedure is rarely or never performed in the non-facility setting |
| 22 | `NON_FAC_PRACTICE_EXP_RVU_NBR` | DOUBLE |  |  | RVU for fully-implemented resource based practice expense for the non-facility setting |
| 23 | `PFT_RVU_CONTENT_ID` | DOUBLE | NOT NULL |  | Unique Identifier for content developed to determine the standard Medicare Fee Schedule. |
| 24 | `PHYS_SUPERVISION_DIAG_PROC_CD` | DOUBLE | NOT NULL |  | Used in post payment review. |
| 25 | `POSTOPERATIVE_PCT` | DOUBLE |  |  | Percentage for postoperative portion of global package that is provided in the office after discharge from the hospital |
| 26 | `PREOPERATIVE_PCT` | DOUBLE |  |  | Percentage for preoperative portion of global package |
| 27 | `PROCEDURE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates whether code is in fee schedule and whether it is separately payable if service is covered. |
| 28 | `PROC_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Identifies HCPCS or CPT4 procedure code. |
| 29 | `PROF_TECH_COMP_INDICATOR_CD` | DOUBLE | NOT NULL |  | Medicare Prof/Tech Component Indicator |
| 30 | `RVU_FLAG` | DOUBLE | NOT NULL |  | Indicates whether or not the Relative Value Unit is for CDM or CPT0 - CPT1 - CDM |
| 31 | `SOURCE_TXT` | VARCHAR(200) |  |  | Contains the Identifier of the Charge Master Description(CDM), Current Procedural Terminology (CPT) and HCPCS. When new nomenclature content is loaded in the middle of the year, nomenclature ids don¿t match for the same source identifiers, so instead of qualifying on nomenclature ids in Revenue GSR we want to qualify on Source Identifier itself. |
| 32 | `TEAM_SURGERY_CD` | DOUBLE | NOT NULL |  | Indicates services for which team surgeons may be paid. |
| 33 | `TOTAL_FACILITY_RVU_NBR` | DOUBLE |  |  | Sum of work, fully implemented facility practice expense, and malpractice expense RVUs |
| 34 | `TOTAL_NON_FAC_RVU_NBR` | DOUBLE |  |  | Sum of work, fully implemented non-facility practice expense, and malpractice expense RVUs |
| 35 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `WORK_RVU_NBR` | DOUBLE |  |  | RVU for physician work |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `MOD_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PROC_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

