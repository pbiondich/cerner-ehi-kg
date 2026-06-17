# BR_CKI_MATCH

> Stores the matched values from the CKI Mapping wizard

**Description:** BR CKI Match  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CKI_MATCH_ID` | DOUBLE | NOT NULL |  | Unique id for the table |
| 2 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 3 | `CLIENT_ID` | DOUBLE | NOT NULL | FK→ | Unique id for the client (BR_CKI_CLIENT) |
| 4 | `CONCEPT_CKI` | VARCHAR(50) |  |  | CKI value that was matched to the client's data item |
| 5 | `DATA_ITEM` | VARCHAR(20) |  |  | String identifier for the client's data item that was matched. |
| 6 | `DATA_ITEM_NAME` | VARCHAR(100) |  |  | Name of the clients data item that was matched |
| 7 | `DATA_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique id for the data type (BR_CKI_DATA_TYPE) |
| 8 | `MILLENNIUM_NAME` | VARCHAR(100) |  |  | Name of the millennium item that was matched to the client data item |
| 9 | `MILLENNIUM_VALUE` | DOUBLE | NOT NULL |  | Unique id of the millennium item that was matched to the client data item |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLIENT_ID` | [BR_CKI_CLIENT](BR_CKI_CLIENT.md) | `CLIENT_ID` |
| `DATA_TYPE_ID` | [BR_CKI_DATA_TYPE](BR_CKI_DATA_TYPE.md) | `DATA_TYPE_ID` |

