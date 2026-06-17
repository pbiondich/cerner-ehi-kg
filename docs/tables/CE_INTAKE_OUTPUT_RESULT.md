# CE_INTAKE_OUTPUT_RESULT

> This table can be used to quickly determine the Intake / Output balance information for a given period.

**Description:** Clinical Event Intake / Output Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_IO_RESULT_ID` | DOUBLE | NOT NULL |  | SEQUENCE_NAME:OCF_SEQ Unique identifier generated for each row of this table. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Encounter. FK from ENCOUNTER table |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifies a logical intake output result. There may be more than one row with the same event_id and io_dt_tm values, but only one of those rows will be current as indicated by the valid_until_dt_tm field. Foreign Key: XFK2 - (Clinical event) SEQUENCE NAME:CLINICAL_EVENT_SEQ |
| 4 | `IO_END_DT_TM` | DATETIME |  |  | The clinical end date and time of the I&O activity. |
| 5 | `IO_RESULT_ID` | DOUBLE | NOT NULL |  | This column will receive a fresh value from the OCF_SEQ sequence. It uniquely identifies a logical intake output result row. There may be more than one row with the same IO_RESULT_ID, but only one of those rows will be current as indicated by the valid_until_dt_tm field. |
| 6 | `IO_START_DT_TM` | DATETIME | NOT NULL |  | The clinical start date and time of the I&O activity. |
| 7 | `IO_STATUS_CD` | DOUBLE | NOT NULL |  | CODE SET:4000160 Indicates whether a clinician has accepted the measurement or not. Current valid values are accepted and rejected. |
| 8 | `IO_TYPE_FLAG` | DOUBLE | NOT NULL |  | States whether the data is patient intake or output. 0=Not Defined, 1=Intake, 2=Output |
| 9 | `IO_VOLUME` | DOUBLE |  |  | The volume of intake or output. The volume unit must be 'ml' from code_set 54. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. Identifies person who is associated with the intake output result. SEQUENCE NAME:PERSON_ONLY_SEQ |
| 11 | `REFERENCE_EVENT_CD` | DOUBLE | NOT NULL |  | The event_cd of the REFERENCE_EVENT_ID result. |
| 12 | `REFERENCE_EVENT_ID` | DOUBLE | NOT NULL |  | The result that contributed to the Intgake or Output result. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 19 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the End Point of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

