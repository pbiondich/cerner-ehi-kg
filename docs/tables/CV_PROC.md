# CV_PROC

> Activity table storing below the line information for CV orders

**Description:** CV Procedure  
**Table type:** ACTIVITY  
**Primary key:** `CV_PROC_ID`  
**Columns:** 30  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) | NOT NULL |  | From ACCESSION. Identifies an order or group of orders. This is an alpha-numeric field. |
| 2 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ACCESSION |
| 3 | `ACTION_DT_TM` | DATETIME |  |  | Date and time the action was done. |
| 4 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | The activity subtype of the associated order (e.g. Echo, Non-Invasive Vascular) |
| 5 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Foreign key to ORDER_CATALOG. The internal code of the order catalog item. |
| 6 | `CV_PROC_ID` | DOUBLE | NOT NULL | PK | Primary key for rows in this table. |
| 7 | `ED_REVIEW_IND` | DOUBLE | NOT NULL |  | This is used as a flag to say whether or not an interpretation was ED reviewed. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ENCOUNTER. Encounter during which the procedure took place. |
| 9 | `GROUP_EVENT_ID` | DOUBLE | NOT NULL |  | The event_id on clinical_event of the procedure grouper event. |
| 10 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | States whether the result is normal, critical or abnormal |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ORDERS |
| 12 | `ORDER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to PRSNL. The physician who ordered the procedure |
| 13 | `ORIG_ORDER_DT_TM` | DATETIME |  |  | The original order date and time for this order |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to PERSON. Person who is the subject of the procedure. |
| 15 | `PHYS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from table PRSNL_GROUP |
| 16 | `PRIM_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to PRSNL. The Primary physician for this person or procedure |
| 17 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | Priority of the order |
| 18 | `PROC_INDICATOR` | VARCHAR(12) |  |  | Procedure Indicator - supporting HEMO availability and others when needed in the future |
| 19 | `PROC_STATUS_CD` | DOUBLE | NOT NULL |  | Department status for the procedure |
| 20 | `REASON_FOR_PROC` | VARCHAR(255) |  |  | Text comments - Reason for the procedure |
| 21 | `REFER_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to PRSNL. The physician who referred the patient for the procedure |
| 22 | `REQUEST_DT_TM` | DATETIME |  |  | The time requested in the order for the start of the first procedural step |
| 23 | `SEQUENCE` | DOUBLE | NOT NULL |  | Ordinal position of procedure within case |
| 24 | `STRESS_ECG_STATUS_CD` | DOUBLE | NOT NULL |  | Status of Stress ECG portion of a procedure with Stress ECG steps. |
| 25 | `STUDY_STATE_CD` | DOUBLE |  |  | A code that Indicates the state of the Procedure with respect to Exam Complete |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PHYS_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRIM_PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REFER_PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CV_MED_R](CV_MED_R.md) | `CV_PROC_ID` |
| [CV_STEP](CV_STEP.md) | `CV_PROC_ID` |
| [CV_STEP_SCHED](CV_STEP_SCHED.md) | `CV_PROC_ID` |

