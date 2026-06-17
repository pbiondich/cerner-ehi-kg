# BR_CKI_CLIENT_DATA

> Stores client data to be matched to a concept cki for each data type

**Description:** Bedrock CKI Client Data  
**Table type:** REFERENCE  
**Primary key:** `BR_CKI_CLIENT_DATA_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CKI_CLIENT_DATA_ID` | DOUBLE | NOT NULL | PK | Unique id for the table |
| 2 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 3 | `CLIENT_ID` | DOUBLE | NOT NULL | FK→ | Unique id for the client (BR_CKI_CLIENT) |
| 4 | `DATA_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique id for the data type (BR_CKI_DATA_TYPE) |
| 5 | `FIELD_CNT` | DOUBLE | NOT NULL |  | Count of number of field rows for this client data |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLIENT_ID` | [BR_CKI_CLIENT](BR_CKI_CLIENT.md) | `CLIENT_ID` |
| `DATA_TYPE_ID` | [BR_CKI_DATA_TYPE](BR_CKI_DATA_TYPE.md) | `DATA_TYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_CKI_CLIENT_DATA_FIELD](BR_CKI_CLIENT_DATA_FIELD.md) | `BR_CKI_CLIENT_DATA_ID` |

