# BB_MOD_DEVICE

> Stores a list of devices associated with a modification option.

**Description:** Blood Bank Modification Device  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE |  |  | Indicates if this device is the default device for the modification option. |
| 2 | `DEVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The code value that uniquely identifies a device type. |
| 3 | `MAX_CAPACITY` | DOUBLE |  |  | Defines the maximum capacity for the device. |
| 4 | `MODIFICATION_DURATION` | DOUBLE |  |  | Defines the standard modification time duration to be added to the modification start time in order to default the modification stop time. |
| 5 | `OPTION_ID` | DOUBLE | NOT NULL | FK→ | The internal system assigned number that uniquely identifies a modification option. |
| 6 | `START_STOP_TIME_IND` | DOUBLE |  |  | Indicates if the system requires a start/stop time to be entered for the modification. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPTION_ID` | [BB_MOD_OPTION](BB_MOD_OPTION.md) | `OPTION_ID` |

