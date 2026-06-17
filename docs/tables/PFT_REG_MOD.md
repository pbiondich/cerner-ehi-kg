# PFT_REG_MOD

> Tracks modifications by type. (i.e. Encounter Type Change, Primary Health Plan Change, Nurse Unit Location Change and Admit Date Time Change.

**Description:** ProFit Account Management  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The date and time that the row was created. |
| 6 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the person responsible for creating a row in the PFT_REG_MOD table. |
| 7 | `DISCH_DT_TM` | DATETIME |  |  | The actual date/time that the patient was discharged from the facility. For most outpatients, this column may be null unless the user process requires capturing this data, for example, day surgery. Auto discharge will populate this column. This also may or may not be a system assigned date and time depending on the discharge process used. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Encounter. This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 10 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). The values in this codeset all have Cerner defined meanings. |
| 11 | `GUARANTOR_ID` | DOUBLE | NOT NULL | FK→ | The person guarantor for patient |
| 12 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related health plan. This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 13 | `INPATIENT_ADMIT_DT_TM` | DATETIME |  |  | Stores the date and time of the inpatient admit. |
| 14 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Contains the current patient location with a location type of facility. |
| 15 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | This field is the current patient location with a location type of nurse unit. |
| 16 | `PFT_REG_MOD_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a modification in the registration. Contains a unique generated number that identifies a single row on the PFT_REG_MOD table. |
| 17 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | This is a numeric number used to represent the order in which to consider this health plan for reimbursement, if the person is a member of more than one health plan. This number may change from the original number depending on the encounter. |
| 18 | `REG_DT_TM` | DATETIME |  |  | Inidcates the date/time that the registration or admission process was performed |
| 19 | `TRANSACTION_TYPE` | VARCHAR(4) |  |  | The type of transaction that occurred. Example: UPDT, ATDS, etc. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `GUARANTOR_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

