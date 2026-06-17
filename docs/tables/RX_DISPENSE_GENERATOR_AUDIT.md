# RX_DISPENSE_GENERATOR_AUDIT

> Table used to audit asynchronized transactions for Pharmacy Dispense Generator service.

**Description:** Pharmacy Dispense Generator Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_NAME` | VARCHAR(50) | NOT NULL |  | Describes the dispense type of the initiating dispense event. |
| 2 | `CORRELATION_UID` | VARCHAR(36) | NOT NULL |  | The identifier for a transaction to the PharmacyDispenseGenerator service. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | This is the date and time the row was created. |
| 4 | `INITIATING_DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the dispense event from which this action is initiated. |
| 5 | `MESSAGE_TXT` | VARCHAR(1000) | NOT NULL |  | Text indicating success or failure messages. |
| 6 | `RX_DISPENSE_GENERATOR_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_DISPNSE_GENERATOR_AUDIT table. |
| 7 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of the transaction. 1 - success, 0 - fail |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INITIATING_DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |

