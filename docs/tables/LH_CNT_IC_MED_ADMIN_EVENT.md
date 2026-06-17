# LH_CNT_IC_MED_ADMIN_EVENT

> Stores the records of Medication administration event

**Description:** Lh_Cnt_Ic_Med_Admin_Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The order catalog of the administered order |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row is created |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter which the order is associated with |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | The ID of the clinical event associated to this medication admin event. |
| 6 | `FACILITY_CD` | DOUBLE | NOT NULL |  | The facility of the user is using to enter medication admin event |
| 7 | `LH_CNT_IC_MED_ADMIN_EVENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_MED_ADMIN_EVENT table. |
| 8 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The nurse unit of the user is using to enter medication admin event |
| 9 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order associated to this med admin event |
| 10 | `ROUTE_CD` | DOUBLE | NOT NULL |  | The route of the administered order |
| 11 | `TEMPLATE_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order Id for the template order. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VERIFICATION_DT_TM` | DATETIME |  |  | The date and time the administration of the order took place |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `TEMPLATE_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

