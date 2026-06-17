# SN_PICKLIST_REQUEST_PC

> Defines the quantity requested from a preference card

**Description:** Surginet Picklist Request Preference Card  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HOLD_QTY` | DOUBLE | NOT NULL |  | The quantity of the requested item that should be picked, but not opened |
| 2 | `OPEN_QTY` | DOUBLE | NOT NULL |  | The quantity of the requested item that should be picked and opened |
| 3 | `PREF_CARD_ID` | DOUBLE | NOT NULL | FK→ | The preference card id that contains the requested quantity information |
| 4 | `REQUEST_QTY` | DOUBLE | NOT NULL |  | The total quantity of the requested item that should be picked |
| 5 | `SN_PICKLIST_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The request row that the preference card data is for |
| 6 | `SN_PICKLIST_REQUEST_PC_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `SN_PREF_CARD_ID` | DOUBLE |  | FK→ | A foreign key to the sn_pref_card table. This field will be zero or null if the pref_card_id fild is populated. the pref_card_id OR the sn_pref_card_id should be filled out (which one is filled out will tell us which model - old or new - was used for the given picklist) |
| 8 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | FK→ | The surgical procedure that the item is being requested for |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREF_CARD_ID` | [PREFERENCE_CARD](PREFERENCE_CARD.md) | `PREF_CARD_ID` |
| `SN_PICKLIST_REQUEST_ID` | [SN_PICKLIST_REQUEST](SN_PICKLIST_REQUEST.md) | `SN_PICKLIST_REQUEST_ID` |
| `SN_PREF_CARD_ID` | [SN_PREF_CARD](SN_PREF_CARD.md) | `SN_PREF_CARD_ID` |
| `SURG_CASE_PROC_ID` | [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_PROC_ID` |

