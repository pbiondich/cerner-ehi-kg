# MM_TRANS_GL

> Mat Mgmt General Ledger Transaction

**Description:** MM TRANS GL  
**Table type:** ACTIVITY  
**Primary key:** `MM_TRANS_GL_ID`  
**Columns:** 34  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_TYPE_CD` | DOUBLE | NOT NULL |  | The type of additional amount from the ADDITIONAL_AMOUNT table. |
| 2 | `AMOUNT` | DOUBLE |  |  | Additional Amount |
| 3 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 5 | `CREATE_ID` | DOUBLE | NOT NULL |  | User id of person which created this row |
| 6 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 7 | `FROM_COMPANY_CODE` | VARCHAR(16) |  |  | The company code defined in the Org tool while defining the organization alias. |
| 8 | `FROM_COST_CENTER_CD` | DOUBLE | NOT NULL |  | The cost center from which the transaction originated. |
| 9 | `FROM_COST_CENTER_DESC` | VARCHAR(60) |  |  | The description of the cost center from which the transaction originated. |
| 10 | `FROM_COST_CENTER_DISP` | VARCHAR(40) |  |  | The display value of the cost center from which the transaction originated. |
| 11 | `FROM_ORG_ID` | DOUBLE | NOT NULL |  | The organization from which the transaction originated. |
| 12 | `FROM_ORG_NAME` | VARCHAR(100) |  |  | The name of the organization from which the transaction originated. |
| 13 | `FROM_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The sub account from which the transaction originated. |
| 14 | `FROM_SUB_ACCOUNT_DESC` | VARCHAR(60) |  |  | The description of the sub account from which the transaction originated. |
| 15 | `FROM_SUB_ACCOUNT_DISP` | VARCHAR(40) |  |  | The display value of the sub account from which the transaction originated. |
| 16 | `MM_PROJECT_NBR_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | The project associated to this group of transactions. |
| 17 | `MM_TRANS_GL_ID` | DOUBLE | NOT NULL | PK | Unique, generated key for MM_TRANS_GL. |
| 18 | `MM_TRANS_LINE_ID` | DOUBLE | NOT NULL | FK→ | Transaction Line ID |
| 19 | `TO_COMPANY_CODE` | VARCHAR(16) |  |  | The target company code defined in the Org tool while defining the organization alias. |
| 20 | `TO_COST_CENTER_CD` | DOUBLE | NOT NULL |  | The target cost center for the transaction. |
| 21 | `TO_COST_CENTER_DESC` | VARCHAR(60) |  |  | The description of the target cost center for the transaction. |
| 22 | `TO_COST_CENTER_DISP` | VARCHAR(40) |  |  | The display value of the target cost center for the transaction. |
| 23 | `TO_ORG_ID` | DOUBLE | NOT NULL |  | The target organization for the transaction. |
| 24 | `TO_ORG_NAME` | VARCHAR(100) |  |  | The name of the target organization for the transaction. |
| 25 | `TO_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The target sub account for the transaction. |
| 26 | `TO_SUB_ACCOUNT_DESC` | VARCHAR(60) |  |  | The description of the target sub account for the transaction. |
| 27 | `TO_SUB_ACCOUNT_DISP` | VARCHAR(40) |  |  | The display value for the target sub account for the transaction. |
| 28 | `TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the transaction. |
| 29 | `TRANS_STATUS_CD` | DOUBLE | NOT NULL |  | Code which specifies the status of the transaction. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MM_PROJECT_NBR_TRACKING_ID` | [MM_PROJECT_NBR_TRACKING](MM_PROJECT_NBR_TRACKING.md) | `MM_PROJECT_NBR_TRACKING_ID` |
| `MM_TRANS_LINE_ID` | [MM_TRANS_LINE](MM_TRANS_LINE.md) | `MM_TRANS_LINE_ID` |
| `TRANSACTION_ID` | [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `TRANSACTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_TRANS_ERROR_LOG](MM_TRANS_ERROR_LOG.md) | `MM_TRANS_GL_ID` |

