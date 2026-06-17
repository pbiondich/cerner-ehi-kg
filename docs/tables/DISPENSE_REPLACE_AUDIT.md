# DISPENSE_REPLACE_AUDIT

> Contains auditing information for when a dispense is replaced by a new dispense, or if a dispense failed to be replaced. This table only contains information about mismatching/incorrect item information that was found during redispensing workflows.

**Description:** Dispense Replace Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this record was created. |
| 2 | `DISPENSE_REPLACE_AUDIT_CD` | DOUBLE | NOT NULL |  | Code value containing user-facing messages related to which aspects of replacing a dispense caused a failure or a warning. |
| 3 | `DISPENSE_REPLACE_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DISPENSE_REPLACE_AUDIT table. |
| 4 | `INIT_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the dispense that initiated the redispensing logic. |
| 5 | `REPLACE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that was intended to replace an item on the dispense. |
| 6 | `REPLACE_MANF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The manufacturer item that was intended to replace a manufacturer item on the dispense. |
| 7 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Denotes whether or not an audit event on this table represents a warning or a failure. When a failure exists on this table, the dispense related to the failure prevented a redispense to occur. When warnings exist, a redispense was allowed to occur. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INIT_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `REPLACE_ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `REPLACE_MANF_ITEM_ID` | [MANUFACTURER_ITEM](MANUFACTURER_ITEM.md) | `ITEM_ID` |

