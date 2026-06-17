# DCP_OUTPUT_ROUTE

> DCP OUTPUT ROUTE

**Description:** DCP OUTPUT ROUTE  
**Table type:** REFERENCE  
**Primary key:** `DCP_OUTPUT_ROUTE_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DCP_OUTPUT_ROUTE_ID` | DOUBLE | NOT NULL | PK |  |
| 2 | `PARAM1_CD` | DOUBLE | NOT NULL |  |  |
| 3 | `PARAM2_CD` | DOUBLE | NOT NULL |  |  |
| 4 | `PARAM3_CD` | DOUBLE | NOT NULL |  |  |
| 5 | `PARAM4_CD` | DOUBLE | NOT NULL |  |  |
| 6 | `PARAM5_CD` | DOUBLE | NOT NULL |  |  |
| 7 | `PARAM_CNT` | DOUBLE |  |  |  |
| 8 | `ROUTE_DESCRIPTION` | VARCHAR(100) |  |  |  |
| 9 | `ROUTE_TYPE_FLAG` | DOUBLE |  |  |  |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ORDER_CATALOG](ORDER_CATALOG.md) | `CONSENT_FORM_ROUTING_CD` |
| [ORDER_CATALOG](ORDER_CATALOG.md) | `REQUISITION_ROUTING_CD` |

