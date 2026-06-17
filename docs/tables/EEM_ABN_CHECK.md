# EEM_ABN_CHECK

> This table is used to log all ABN checks performed.

**Description:** EEM ABN Check  
**Table type:** ACTIVITY  
**Primary key:** `ABN_CHECK_ID`  
**Columns:** 62  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_CHECK_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. |
| 2 | `ABN_STATE_CD` | DOUBLE | NOT NULL | FK→ | The state of the ABN. For example: Checked, Signed, Printed, Not Signed, etc. |
| 3 | `ABN_STATE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the ABN State Code. |
| 4 | `ABN_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | The ID associated to the row in this table that is the tracking identifier for this ABN check. |
| 5 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 8 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `BIRTH_DT_TM` | DATETIME |  |  | The date of birth. |
| 11 | `BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding BIRTH_DT_TM column. |
| 12 | `CHECK_SEQ` | DOUBLE | NOT NULL |  | The sequence of the check. |
| 13 | `DIAG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number. |
| 14 | `DIAG_SOURCE_IDENT` | VARCHAR(50) | NOT NULL |  | The identifier of the diagnosis source. |
| 15 | `DIAG_VOCAB_CD` | DOUBLE | NOT NULL |  | The code value for the source vocabulary for the diagnosis. |
| 16 | `DIAG_VOCAB_MEANING` | VARCHAR(12) |  |  | A text representation of the meaning for DIAG_VOCAB_CD. |
| 17 | `DUP_CHECK_IND` | DOUBLE | NOT NULL |  | Indicates if there is duplicate checking. |
| 18 | `DUP_KEY` | VARCHAR(255) |  |  | Duplicate Key column |
| 19 | `EDI_TRANSACTION_IDENT` | VARCHAR(50) |  |  | Unique identifier provided by transaction services to uniquely identify a call to transaction services for medical necessity check. |
| 20 | `EEM_FILE_ID` | DOUBLE | NOT NULL | FK→ | The ID of the row in EEM_FILE related to this ABN check. |
| 21 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 22 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 23 | `EST_SERVICE_IND` | DOUBLE | NOT NULL |  | An indicator for estimated service. |
| 24 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification used for a given encounter. Examples may include Worker's Comp, Self Pay, etc. |
| 25 | `GENDER_CD` | DOUBLE | NOT NULL | FK→ | Specifies the gender. |
| 26 | `GENDER_MEANING` | VARCHAR(12) |  |  | A textual representation of the gender. |
| 27 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 28 | `HIGH_STATUS_CD` | DOUBLE | NOT NULL | FK→ | The high status code. Examples are Form Required or Form Not Required. |
| 29 | `HIGH_STATUS_MEANING` | VARCHAR(12) |  |  | A textual representation of the high status. |
| 30 | `INPATIENT_IND` | DOUBLE | NOT NULL |  | Indicates if the check is for an inpatient or not. |
| 31 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The Location that the procedure was checked against. |
| 32 | `MED_STATUS_CD` | DOUBLE | NOT NULL | FK→ | The medium status code for the ABN check. For example, meets medical necessity, Does not meet Medical Necessity, policy not defined, ambiguous, etc. |
| 33 | `MED_STATUS_MEANING` | VARCHAR(12) |  |  | A text representation of the meaning for MED_STATUS_CD. |
| 34 | `PARENT1_ID` | DOUBLE | NOT NULL |  | Id of table 1 the ABN check is associated to. |
| 35 | `PARENT1_TABLE` | VARCHAR(30) |  |  | The name of the parent 1 table the ABN check is associated to. |
| 36 | `PARENT2_ID` | DOUBLE | NOT NULL |  | The Id of the parent 2 table the ABN check is associated to. |
| 37 | `PARENT2_TABLE` | VARCHAR(30) |  |  | The name of the parent 2 table the ABN check is associated to. |
| 38 | `PARENT3_ID` | DOUBLE | NOT NULL |  | The Id of the parent 3 table the ABN check is associated to. |
| 39 | `PARENT3_TABLE` | VARCHAR(30) |  |  | The name of the parent 3 table the ABN check is associated to. |
| 40 | `PARENT_MNEMONIC` | VARCHAR(100) |  |  | A mnemonic for the parent the ABN check is associated to. |
| 41 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 42 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 43 | `PROC_DISPLAY_ID` | DOUBLE | NOT NULL |  | Identifier where the procedure display is linked to (appt_synonym_cd/synonym_id) |
| 44 | `PROC_DISPLAY_TABLE` | VARCHAR(30) |  |  | Identifies the table where the procedure display is linked to (CODE_VALUE/ORDER_CATALOG_SYNONYM) |
| 45 | `PROC_GROUP_DISPLAY_ID` | DOUBLE | NOT NULL |  | The Id of the procedure group display associated to the ABN check. |
| 46 | `PROC_GROUP_DISPLAY_TABLE` | VARCHAR(30) |  |  | The table name associated with the procedure group display. E.G. CODE_VALUE, etc. |
| 47 | `PROC_GROUP_PARENT_ID` | DOUBLE | NOT NULL |  | The Id of the procedure group parent. |
| 48 | `PROC_GROUP_PARENT_TABLE` | VARCHAR(30) |  |  | The table name of the procedure group parent. |
| 49 | `PROC_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number. |
| 50 | `PROC_PARENT_ID` | DOUBLE | NOT NULL |  | Identifier where then procedures are linked to (appt_type_cd/catalog_cd) |
| 51 | `PROC_PARENT_TABLE` | VARCHAR(30) |  |  | Identifies the table where the procedures are linked to (i.e. CODE_VALUE) |
| 52 | `PROC_SOURCE_IDENT` | VARCHAR(50) | NOT NULL |  | The identifier of the procedure source. |
| 53 | `PROC_VOCAB_CD` | DOUBLE | NOT NULL | FK→ | The source vocabulary for the procedure. |
| 54 | `PROC_VOCAB_MEANING` | VARCHAR(12) |  |  | The textual representation of the PROC_VOCAB_CD. |
| 55 | `SERVICE_DT_TM` | DATETIME |  |  | The service date and time for the ABN check. |
| 56 | `SPONSOR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 57 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `USE_SERVICE_IND` | DOUBLE | NOT NULL |  | Use Service Date and Time Indicator |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ABN_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ABN_TRACKING_ID` | [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `ABN_CHECK_ID` |
| `DIAG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `EEM_FILE_ID` | [EEM_FILE](EEM_FILE.md) | `EEM_FILE_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `GENDER_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `HIGH_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `MED_STATUS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROC_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PROC_VOCAB_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SPONSOR_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [EEM_ABN_ACTION](EEM_ABN_ACTION.md) | `ABN_CHECK_ID` |
| [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `ABN_TRACKING_ID` |
| [EEM_ABN_DIAG](EEM_ABN_DIAG.md) | `ABN_CHECK_ID` |
| [EEM_ABN_INDEX](EEM_ABN_INDEX.md) | `ABN_CHECK_ID` |
| [EEM_ABN_LOW](EEM_ABN_LOW.md) | `ABN_CHECK_ID` |
| [EEM_ABN_MOD](EEM_ABN_MOD.md) | `ABN_CHECK_ID` |

