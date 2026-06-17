# OMF_SVC_CAT_HIST_ST

> omf_svc_cat_hist_st

**Description:** Stores service category history for each encounter.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 49

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANESTHESIOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the anesthesiologist for the principal procedure. |
| 2 | `ANESTH_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the anesthesiologist. |
| 3 | `ATTEND_PHYS_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the attending physician. |
| 4 | `ATT_PRSNL_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of attending physicians as defined within the OMFGroupingTool.exe. |
| 5 | `ATT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the attending physician. |
| 6 | `ATT_PRSNL_MED_SPEC_CD` | DOUBLE | NOT NULL |  | Grouping of attending physicians as defined within the OMFGroupingTool.exe. |
| 7 | `BEG_TRANSACTION_DT_NBR` | DOUBLE |  |  | The Julian date for the beginning date of the service category. |
| 8 | `BEG_TRANSACTION_DT_TM` | DATETIME |  |  | The date/time for the beginning date of the service category. |
| 9 | `BEG_TRANSACTION_MIN_NBR` | DOUBLE |  |  | The minute for the beginning date/time of the service category. |
| 10 | `BEG_TRANSACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `CPT_P_STR` | VARCHAR(255) |  |  | Free text string of cpt procedure codes. |
| 12 | `DEATH_24H_PRIN_PROC_IND` | DOUBLE |  |  | Indicates whether or not the patient expired within 24 hours of the principal procedure. |
| 13 | `DRG_AMLOS` | DOUBLE |  |  | The arithmetic mean length of stay based on the DRG. |
| 14 | `DRG_GMLOS` | DOUBLE |  |  | The geometric mean length of stay based on the DRG. |
| 15 | `DRG_GRP2_CD` | DOUBLE | NOT NULL |  | Grouping of DRG codes as defined within the OMFGroupingTool.exe. |
| 16 | `DRG_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of DRG codes as defined within the OMFGroupingTool.exe. |
| 17 | `DRG_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the DRG code. |
| 18 | `DRG_WEIGHT` | DOUBLE |  |  | The relative weight of the DRG. |
| 19 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 20 | `END_TRANSACTION_DT_NBR` | DOUBLE |  |  | The Julian date for the end of the service category. |
| 21 | `END_TRANSACTION_DT_TM` | DATETIME |  |  | The date/time for the end of the service category. |
| 22 | `END_TRANSACTION_MIN_NBR` | DOUBLE |  |  | The minute for the end of the service category. |
| 23 | `END_TRANSACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 24 | `ICD9_SECONDARY1_DIAG_NOMEN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the secondary diagnosis code. |
| 25 | `ICD_PD_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of diagnosis codes as defined within the OMFGroupingTool.exe |
| 26 | `ICD_PD_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the primary diagnosis code. |
| 27 | `ICD_PP_DT_NBR` | DOUBLE |  |  | The Julian date for the principal procedure. |
| 28 | `ICD_PP_DT_TM` | DATETIME |  |  | The date/time of the principal procedure. |
| 29 | `ICD_PP_DT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 30 | `ICD_PP_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of procedures as defined within the OMFGroupingTool.exe |
| 31 | `ICD_PP_MINUTES` | DOUBLE |  |  | The number of procedure minutes. |
| 32 | `ICD_PP_MIN_NBR` | DOUBLE |  |  | The minute of the principal procedure. |
| 33 | `ICD_PP_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the principal procedure. |
| 34 | `ICD_SD_STR` | VARCHAR(255) |  |  | Free text string of secondary diagnosis codes. |
| 35 | `ICD_SP_STR` | VARCHAR(255) |  |  | Free text string of secondary procedures. |
| 36 | `MDC_CD` | DOUBLE | NOT NULL |  | The major diagnostic category associated with the DRG. |
| 37 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 38 | `PREV_SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The previous service category. |
| 39 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the current category of service the patient is receiving for this encounter. |
| 40 | `SURGEON_GRP_CD` | DOUBLE | NOT NULL |  | Grouping of surgeons as defined within the OMFGroupingTool.exe |
| 41 | `SURGEON_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the surgeon. |
| 42 | `SURGEON_MED_SPEC_CD` | DOUBLE | NOT NULL |  | Grouping of physicians as defined within the OMFGroupingTool.exe. |
| 43 | `SURGEON_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the surgeon. |
| 44 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL |  | Unique identifier for the service_category_hist table. |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANESTHESIOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ATT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `SURGEON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

