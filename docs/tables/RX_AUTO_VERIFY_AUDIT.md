# RX_AUTO_VERIFY_AUDIT

> The table is used to log information relevant to decisions made by system around pharmacy product assignment and verification.

**Description:** Pharmacy auto verify audit table.  
**Table type:** ACTIVITY  
**Primary key:** `RX_AUTO_VERIFY_AUDIT_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | Personnel id of the user who is taking the action on the order. |
| 2 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | Order action sequence that is performed on the order. |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Order action that is performed on the order. |
| 4 | `AUTO_VERIFY_FAIL_REASON_CD` | DOUBLE | NOT NULL |  | Codified values for rx auto verification failure reasons. |
| 5 | `CATALOG_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier used to trace back to rx_product_assign_group_audit, rx_product_assign_item_audit, and rx_product_assign_audit tables for the order that is being tried for rx auto product assign. |
| 6 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | The code value of the communication type between ordering provider and action personnel. |
| 7 | `DISCERN_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Flag representing current order catalog's auto verification settings for Discern Alerts. For IV set, this is the flag on the catalog of the matching IV set. |
| 8 | `DISPENSE_STATUS_FLAG` | DOUBLE | NOT NULL |  | Rx dispense status flag:0: not set 1: Rx dispense service is called, but dispense is not guaranteed to be successful 2: Rx dispense service is not called |
| 9 | `IC_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Flag representing current order catalog's auto verification settings for Interaction Checking. For IV set, this is the flag on the catalog of the matching IV set. |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL |  | Order ID to which this record is associated. |
| 11 | `ORDER_PROVIDER_AV_PRIV_FLAG` | DOUBLE | NOT NULL |  | Order provider's Auto Verification privilege |
| 12 | `ORDER_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Personnel_id of the ordering physician who authorizes the action on the order. |
| 13 | `PRODUCT_ASSIGN_STATUS_FLAG` | DOUBLE | NOT NULL |  | Rx auto product assign status flag |
| 14 | `PRSNL_AUTO_VERIFY_PRIV_FLAG` | DOUBLE | NOT NULL |  | Auto Verification privilege (RXAUTOVERIFY) of the user who is taking the action:0: not set. Privilege for Auto Verification has not been evaluated when the record is written.1: privilege for Auto Verification is considered on for this order 2: privilege for Auto Verification is considered off for this order |
| 15 | `PRSNL_RX_VERIFY_PRIV_FLAG` | DOUBLE | NOT NULL |  | Rx Verify privilege (RXVERIFY) of the user who is taking the action:0: not set. Privilege for Rx verify has not been evaluated when the record is written.1: Rx Verify privilege is on 2: Rx Verify privilege is off |
| 16 | `RX_AUTO_VERIFY_AUDIT_ID` | DOUBLE | NOT NULL | PK | Unique identifier for rx auto verification audit. |
| 17 | `STATUS_STRING` | VARCHAR(2000) | NOT NULL |  | Text description of the status of rx auto product verification. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CATALOG_GROUP_ID` | [RX_PRODUCT_ASSIGN_GROUP_AUDIT](RX_PRODUCT_ASSIGN_GROUP_AUDIT.md) | `CATALOG_GROUP_ID` |
| `ORDER_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_AUTO_VERIFY_ING_AUDIT](RX_AUTO_VERIFY_ING_AUDIT.md) | `RX_AUTO_VERIFY_AUDIT_ID` |

