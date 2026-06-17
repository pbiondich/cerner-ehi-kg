# DRG

> Stores fields like nomenclaure code, drg payor code and contributor system code

**Description:** Stores the DRG codes for a coded chart.  
**Table type:** ACTIVITY  
**Primary key:** `DRG_ID`  
**Columns:** 35  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMORBIDITY_CD` | DOUBLE | NOT NULL |  | Identifies the comorbidity tier of the grouper. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that the row was created |
| 9 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The Person who created the row |
| 10 | `DRG_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the DRG table. It is an internal system assigned number |
| 11 | `DRG_PAYMENT` | DOUBLE |  |  | This is the expected payment for this DRG |
| 12 | `DRG_PAYOR_CD` | DOUBLE | NOT NULL |  | Identifies the payer for the grouper. |
| 13 | `DRG_PRIORITY` | DOUBLE |  |  | This is the priority or order that we received the drg's (1,2,3¿ primary being 1) |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 15 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Identifies an Encounter as it relates to a time slice. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `GROUPER_CD` | DOUBLE | NOT NULL |  | This is the grouper that was used to calculate the estimated reimbursement. |
| 18 | `MDC_APR_CD` | DOUBLE | NOT NULL |  | The code values for Major Diagnosis Code for 3Ms APR-DRG codes. |
| 19 | `MDC_CD` | DOUBLE | NOT NULL |  | The code values for Major Diagnosis Code |
| 20 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number |
| 21 | `OUTLIER_COST` | DOUBLE |  |  | Indicates the difference in cost for the grouper vs. average cost. |
| 22 | `OUTLIER_DAYS` | DOUBLE |  |  | Indicates the difference in days for the grouper vs. average number of days. |
| 23 | `OUTLIER_REIMBURSEMENT_COST` | DOUBLE |  |  | Indicates the difference in reimbursement cost for the grouper vs. average reimbursement cost. |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key ID from the parent table. |
| 25 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent table name. |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 27 | `RISK_OF_MORTALITY_CD` | DOUBLE | NOT NULL |  | This is the code_value for risk of mortality |
| 28 | `SEVERITY_OF_ILLNESS_CD` | DOUBLE | NOT NULL |  | This is the code_value for severity of illness |
| 29 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | The code values for source_vocabulary |
| 30 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier for the service category history table. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DRG_ENCNTR_EXTENSION](DRG_ENCNTR_EXTENSION.md) | `DRG_ID` |

