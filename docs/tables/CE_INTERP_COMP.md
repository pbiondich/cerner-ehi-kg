# CE_INTERP_COMP

> ce interp comp

**Description:** ce interp comp  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMP_EVENT_ID` | DOUBLE | NOT NULL |  | The combination of the Comp Event ID and the Comp Event Version Nbr is the primary key of the result record that is used as an operand for the interp result. |
| 2 | `COMP_IDX` | DOUBLE | NOT NULL |  | A sequence nbr used to make the primary key unique. |
| 3 | `COMP_NAME` | VARCHAR(200) |  |  | Name of the component used in the calculation_equation. For example for an equation like MAP = SAP + (DAP x 2)/3 , comp_name would be SAP or DAP. |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the Event Table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when this row is valid. |
| 11 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

