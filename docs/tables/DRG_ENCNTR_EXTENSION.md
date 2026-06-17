# DRG_ENCNTR_EXTENSION

> Encounter level DRG informantion such as weight, desc...

**Description:** DRG ENCNTR EXTENSION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALOS` | DOUBLE |  |  | This is the alos assigned for this DRG |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CASE_RESOURCE_WEIGHT` | DOUBLE |  |  | This is the assigned case resource weight |
| 8 | `COMPLEXITY_OVERLAY` | DOUBLE |  |  | This is the assigned complexity overlay assigned to this DRG |
| 9 | `COMPLEXITY_OVERLAY_TEXT` | VARCHAR(255) |  |  | This is the text that was assigned by the encoder and passed into Cerner systems. |
| 10 | `DAY_THRESHOLD` | DOUBLE |  |  | This is the day threshold that was assigned by the encoder and passed into Cerner systems. |
| 11 | `DRG_ENCNTR_EXTENSION_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for the DRG encounter extension table, it is a system assigned number. |
| 12 | `DRG_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the DRG table. |
| 13 | `DRG_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the drg_specialty table. |
| 14 | `DRG_WEIGHT` | DOUBLE |  |  | Stores the DRG weight for groupers whose weights are not stored in the drg_extension table. Null = Look for the weight in the drg_extension table -1 = Blank Values >= 0 are valid weights. |
| 15 | `ELOS` | DOUBLE |  |  | This is the estimated length of stay that was assigned by the encoder and passed into Cerner systems. |
| 16 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 17 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `EPISODE_CLINICAL_COMPLEX_SCORE` | DOUBLE |  |  | The ECCS is the measure of the cumulative effect of Diagnosis Complexity Level for a specific episode. Episode Clinical Complexity Score (ECCS), which replaces PCCL in AR-DRG v 8.0 and used for reimbursement calculation. |
| 20 | `HIGH_TRIM_VALUE` | DOUBLE |  |  | A figure representing the high trim point of the WIES calculation. |
| 21 | `HOSPITAL_BASE_RATE` | DOUBLE |  |  | This field is only populated when using the 3M Canadian encoder. It is base reimbursement rate for the hospitals |
| 22 | `HRS_MECH_VENT_VALUE` | DOUBLE |  |  | A figure representing a co-payment under WIES, used in accurate calculation of WIES |
| 23 | `LOW_TRIM_VALUE` | DOUBLE |  |  | A figure representing the low trim point of the WIES calculation. |
| 24 | `MCC` | DOUBLE |  |  | This is the MCC that was assigned by the encoder and passed into Cerner systems. |
| 25 | `MCC_TEXT` | VARCHAR(255) |  |  | This is the MCC text that was assigned by the encoder and passed into Cerner systems. |
| 26 | `ONTARIO_CASE_WEIGHT` | DOUBLE |  |  | This is the ontario case weight that was assigned by the encoder and passed into Cerner systems. |
| 27 | `PATIENT_STATUS_CD` | DOUBLE | NOT NULL |  | This is the patient status that was returned from the encoder (i.e. Typical Patient, Transfer patient, Long-stay patient...). |
| 28 | `PERDIEM` | DOUBLE |  |  | This is the Per diem that was assigned by the encoding system. |
| 29 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 30 | `SOURCE_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | This is the source identifier (i.e. the DRG code). |
| 31 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | This is the type of code i.e. CPT, ICD-9-CM... |
| 32 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier for the service category history table. |
| 33 | `TOTAL_EST_REIMB` | DOUBLE |  |  | This is the estimated reimbursement amount for the particular code, returned from the encoder. |
| 34 | `TOTAL_EST_REIMB_VALUE` | DOUBLE |  |  | This field is only populated when using the 3M Canadian encoder. It stores the Ontario case weight except in the case of atypical lengths of stay |
| 35 | `TOTAL_REIMB_VALUE` | DOUBLE |  |  | This field is the actual total reimbursement value if one is collected from the Billing system. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `WIES_FUNDING_AMT` | DOUBLE |  |  | The dollar amount allocated to the provider for healthcare reimbursement. |
| 42 | `WIES_WEIGHT_VALUE` | DOUBLE |  |  | A figure representing the Weighted Inlier Equivalent Separations. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRG_ID` | [DRG](DRG.md) | `DRG_ID` |
| `DRG_SPECIALTY_ID` | [DRG_SPECIALTY](DRG_SPECIALTY.md) | `DRG_SPECIALTY_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

