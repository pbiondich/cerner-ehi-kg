# ORD_RQSTN

> Holds informatin about every assigned request ID.

**Description:** Order Requisition  
**Table type:** ACTIVITY  
**Primary key:** `ORD_RQSTN_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLIENT_ALIAS_NAME` | VARCHAR(6) | NOT NULL |  | The client name of the requested assignment ident. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID to which this request is associated. |
| 3 | `ORD_RQSTN_ID` | DOUBLE | NOT NULL | PK | Unique order requisition identifier about which information is stored. |
| 4 | `RQSTN_ASSIGNMENT_IDENT` | VARCHAR(16) | NOT NULL |  | Request identifier which identifies a group of orders. |
| 5 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Contains the sequence number portion of the requested assignment ident. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ORD_RQSTN_ORD_R](ORD_RQSTN_ORD_R.md) | `ORD_RQSTN_ID` |

