# IO_DEVICE_INTERRUPT

> Stores device interruptions or stoppage event information related to an intake/output device, e.g. infusion pump.

**Description:** IO_DEVICE_INTERRUPT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Encounter. FK from ENCOUNTER table |
| 2 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | Used to identify the method in which a result was entered. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | The parent event id associated with clinical result. EVENT_ID from CLINICAL_EVENT table. |
| 4 | `INTERRUPT_END_DT_TM` | DATETIME | NOT NULL |  | The date and time the IO device stopped experiencing an intteruption in service,i.e. resumed normal normal service operation. |
| 5 | `INTERRUPT_START_DT_TM` | DATETIME | NOT NULL |  | The date and time the IO device began to experience an interruption in service. |
| 6 | `IO_DEVICE_INTERRUPT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `IO_TYPE_FLAG` | DOUBLE | NOT NULL |  | States whether the data is patient intake or output.0 = UNKNOWN1 = INTAKE2 = OUTPUT |
| 8 | `ORDER_ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | Indicates the order action the event was documented against. |
| 9 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Unique foreign key to the ORDERS table. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. Identifies person who is associated with the intake output result. SEQUENCE NAME:PERSON_ONLY_SEQ |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the beginning point in time for when a row in the table is valid. |
| 17 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the end point of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

