# ORDER_PRIORITY_FLEXING

> Controls how the priority order entry field behaves in Powerchart. Includes list filtering, default start date/time, and the ability to disable frequency and duration order entry fields based on which priority is selected.

**Description:** Controls how the priority order entry field behaves in Powerchart.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEFAULT_START_DT_TM` | VARCHAR(20) |  |  | The string defining what the requested start date/time should be defaulted to when the user chooses this priority. Empty mean don't change it. ";" means empty out the date field. "T;N" means default it to the current date/time. |
| 3 | `DISABLE_FREQ_IND` | DOUBLE |  |  | This field defines whether the frequency and duration order entry fields are automatically disabled when the user chooses this priority. |
| 4 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | The order entry format that this flexing record applies to. |
| 5 | `ORDER_PRIORITY_FLEXING_ID` | DOUBLE | NOT NULL |  | The system-assigned unique identifier for this record. |
| 6 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | Priority code value that this flexing record applies to. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

