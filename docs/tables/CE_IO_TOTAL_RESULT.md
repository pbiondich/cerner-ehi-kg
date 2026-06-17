# CE_IO_TOTAL_RESULT

> This table is used to store the Intake/Output Total information for a given period of time.

**Description:** Clinical Events I/O Total Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_IO_TOTAL_RESULT_ID` | DOUBLE | NOT NULL |  | A Unique, generated number that is used to identify an individual IO Total Result |
| 2 | `ENCNTR_FOCUSED_IND` | DOUBLE | NOT NULL |  | Identifies whether the IO Total is encounter focused, meaning that the total only comes from the encntr_id on the table. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | When IO Total is calculated for a specific encounter, encntr_id will be populated. When IO Total calculated for all encounters, encntr_id will be 0. |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifies a logical IO Total Result. There may be more than one row with the same event_id and io_total_dt_tm values, but only one of those rows will be current as indicated by the valid_until_dt_tm field. |
| 5 | `IO_TOTAL_DEFINITION_ID` | DOUBLE | NOT NULL | FK→ | A reference identifier of IO Total Definitions that is sued to calculate the IO Total. |
| 6 | `IO_TOTAL_END_DT_TM` | DATETIME |  |  | The clinical end date/time of the I&O Total. |
| 7 | `IO_TOTAL_RESULT_VAL` | VARCHAR(255) |  |  | The formatted string of the IO Total Value. Example: "100.0000" |
| 8 | `IO_TOTAL_START_DT_TM` | DATETIME |  |  | The clinical start date/time of the I&O Total. |
| 9 | `IO_TOTAL_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure associated to the IO Total Value. |
| 10 | `IO_TOTAL_VALUE` | DOUBLE | NOT NULL |  | The value of the IO Total Result which is calculated by the system and ensured by the user. |
| 11 | `LAST_IO_RESULT_CLINSIG_DT_TM` | DATETIME |  |  | Contains the last clinically significant date time of the intake output result that went into the IO Total. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the Person that the IO Total is associated to. |
| 13 | `SUSPECT_FLAG` | DOUBLE | NOT NULL |  | States whether the IO Total is classified as Suspect. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VALID_FROM_DT_TM` | DATETIME |  |  | Contains the Beginning Point of when a row in the table is valid. |
| 20 | `VALID_UNTIL_DT_TM` | DATETIME |  |  | Contains the end point of when a row in the table is valid. Current version of the result has an open "Until_dt_tm" value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `IO_TOTAL_DEFINITION_ID` | [IO_TOTAL_DEFINITION](IO_TOTAL_DEFINITION.md) | `IO_TOTAL_DEFINITION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

