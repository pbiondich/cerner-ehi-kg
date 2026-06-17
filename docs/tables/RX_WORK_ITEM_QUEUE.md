# RX_WORK_ITEM_QUEUE

> Holds items that need to be worked.

**Description:** Pharmacy Work Item Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the work item was created. |
| 2 | `CREATE_TZ` | DOUBLE | NOT NULL |  | The time zone associated to the CREATE_DT_TM column. |
| 3 | `CURRENT_START_DT_TM` | DATETIME |  |  | The current start date and time associated to the work item. |
| 4 | `CURRENT_START_TZ` | DOUBLE | NOT NULL |  | The time zone associated with the CURRENT_START_DT_TM column. |
| 5 | `DISCHARGE_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time the encounter associated to the work item will be discharged. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter associated to the work item. |
| 7 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The facility associated to the work item. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The logical domain that the work item is associated with. |
| 9 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The medical service related to the work item. |
| 10 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | The nurse unit associated to the work item. |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order associated to the work item. |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The med request that this queue item pertains to. |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The table that has more details about this work item. The only value to start with will be RXS_MED_REQUEST. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person associated to the work item. |
| 15 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority code value for the work item. |
| 16 | `RX_WORK_ITEM_QUEUE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RX_WORK_ITEM_QUEUE table. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `WORK_ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | The type of work item. Examples: ERX, Unverified Order, Med Request |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

