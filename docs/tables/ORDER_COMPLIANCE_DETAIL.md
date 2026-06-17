# ORDER_COMPLIANCE_DETAIL

> Stores detail information about patient compliance for orders that are within the system.

**Description:** Order Compliance Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLIANCE_CAPTURE_DT_TM` | DATETIME | NOT NULL |  | The date/time that compliance information for the order was captured during the compliance conversation. |
| 2 | `COMPLIANCE_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the compliance that was captured according to the information source. For example, not taking, still taking as prescribed, etc. |
| 3 | `INFORMATION_SOURCE_CD` | DOUBLE | NOT NULL |  | The source that provided the information for the order during the compliance conversation. |
| 4 | `LAST_OCCURRED_DT_ONLY_IND` | DOUBLE | NOT NULL |  | Indicates whether the last occurred date/time field has only a valid date (1) or both a valid date and a valid time (0). |
| 5 | `LAST_OCCURRED_DT_TM` | DATETIME |  |  | The last date and time that the patient took a medication, performed a procedure or carried out an order. |
| 6 | `LAST_OCCURRED_TZ` | DOUBLE |  |  | The time zone for the last occurred date time. This time zone is based on the encounter location. |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long text id from the long text table where the comments that were captured for an order during the compliance conversation are stored. |
| 8 | `ORDER_COMPLIANCE_DETAIL_ID` | DOUBLE | NOT NULL |  | The primary key of this table. |
| 9 | `ORDER_COMPLIANCE_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order compliance that the order compliance detail is related to. |
| 10 | `ORDER_NBR` | DOUBLE | NOT NULL |  | The order ID from the orders table for the order that was reviewed during the compliance conversation. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_COMPLIANCE_ID` | [ORDER_COMPLIANCE](ORDER_COMPLIANCE.md) | `ORDER_COMPLIANCE_ID` |

