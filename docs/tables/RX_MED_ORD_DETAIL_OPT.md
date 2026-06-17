# RX_MED_ORD_DETAIL_OPT

> Valid options for an order detail of an item at a facility for an age range.

**Description:** Pharmacy Medical Order Detail Option  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates that this row is to be used for the default. |
| 2 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | Order in which the detail options are to be displayed. |
| 3 | `OPT_CD` | DOUBLE | NOT NULL |  | If the option is from a code set, this field will be populated. For example, if the order entry field is Route, then this will contain a value from code set 4001. |
| 4 | `OPT_NBR` | DOUBLE | NOT NULL |  | This will be used for options that are numeric in nature.Example: Dose |
| 5 | `OPT_TXT` | VARCHAR(100) | NOT NULL |  | This will be used for options that are textual in nature.Example: Free-text Dose |
| 6 | `RX_MED_ORD_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Refers to the field that this option is defined for. |
| 7 | `RX_MED_ORD_DETAIL_OPT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_MED_ORD_DETAIL_OPT table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RX_MED_ORD_DETAIL_ID` | [RX_MED_ORD_DETAIL](RX_MED_ORD_DETAIL.md) | `RX_MED_ORD_DETAIL_ID` |

