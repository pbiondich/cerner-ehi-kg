# ACCEPT_QUAR_REASON

> Contains a list of acceptable quarantined products for an organization.

**Description:** Accept Quarantine Reason  
**Table type:** REFERENCE  
**Primary key:** `ACCEPT_QUAR_REASON_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_QUAR_REASON_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the ACCEPT_QUAR_REASON table. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ORG_SHIPMENT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the ORG_SHIPMENT table. Associates the acceptable quarantined products with an organization. |
| 7 | `QUAR_REASON_CD` | DOUBLE | NOT NULL | FK→ | Contains the quarantine reason code value. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORG_SHIPMENT_ID` | [ORG_SHIPMENT](ORG_SHIPMENT.md) | `ORG_SHIPMENT_ID` |
| `QUAR_REASON_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ACCEPT_QUAR_PROD_R](ACCEPT_QUAR_PROD_R.md) | `ACCEPT_QUAR_REASON_ID` |

