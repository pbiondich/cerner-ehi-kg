# SN_CT_DISPLAY_ROW

> Stores information regarding rows defined to appear ina view type

**Description:** Surginet Case Tracking Display Row  
**Table type:** REFERENCE  
**Primary key:** `SN_CT_DISPLAY_ROW_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ROW_SEQUENCE` | DOUBLE | NOT NULL |  | Defines the order of the rows that have the same sn_ct_view_type_id |
| 2 | `ROW_TYPE_FLAG` | DOUBLE | NOT NULL |  | Defines which type of row this is. 0 - event status type flag. This type of row will contain information defining the behavior of the event bar in dynamic view 1 - data field flag. This type of row will contain information on what case data to display in dynamic view |
| 3 | `SN_CT_DISPLAY_ROW_ID` | DOUBLE | NOT NULL | PK | Primary key for this table |
| 4 | `SN_CT_VIEW_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to sn_ct_view_type to identify which view type this row is defined for |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SN_CT_VIEW_TYPE_ID` | [SN_CT_VIEW_TYPE](SN_CT_VIEW_TYPE.md) | `SN_CT_VIEW_TYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_CT_DISPLAY_FIELD](SN_CT_DISPLAY_FIELD.md) | `SN_CT_DISPLAY_ROW_ID` |

