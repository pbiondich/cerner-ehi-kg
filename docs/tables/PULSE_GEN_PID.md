# PULSE_GEN_PID

> Contains informaton that comes in the Pjlse Generator's PID field (person content). From external source.

**Description:** PULSE Generator PID informaton  
**Table type:** ACTIVITY  
**Primary key:** `PULSE_GEN_PID_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDRESS_TXT` | VARCHAR(150) |  |  | The address in this PID information |
| 2 | `BIRTH_DT_TM_TXT` | VARCHAR(8) |  |  | Text version of The birth date for this PID information in the format: YYYYMMDD |
| 3 | `NAME_FIRST` | VARCHAR(30) |  |  | The first name in the PID information |
| 4 | `NAME_FIRST_KEY` | VARCHAR(30) |  |  | The first name key in the PID information |
| 5 | `NAME_FULL_FORMATTED` | VARCHAR(100) |  |  | The full formatted name for this PID information |
| 6 | `NAME_LAST` | VARCHAR(30) |  |  | The last name in the PID information |
| 7 | `NAME_LAST_KEY` | VARCHAR(30) |  |  | The last name key in the PID information |
| 8 | `NAME_MIDDLE` | VARCHAR(30) |  |  | The middle name in the PID information |
| 9 | `NAME_MIDDLE_KEY` | VARCHAR(30) |  |  | The middle name key in the PID information |
| 10 | `PULSE_GEN_PID_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 11 | `SEX_CD` | DOUBLE | NOT NULL |  | The gender in the PID information |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PULSE_GEN](PULSE_GEN.md) | `PULSE_GEN_PID_ID` |

