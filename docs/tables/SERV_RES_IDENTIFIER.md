# SERV_RES_IDENTIFIER

> Textual Identifiers for the Service Resources that represent Pharmacy locations

**Description:** Service Resource Identifier  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | A unique internal identifier for this service resource |
| 2 | `SERV_RES_IDENTIFIER_ID` | DOUBLE | NOT NULL |  | Unique id for Serv_res_identifier table |
| 3 | `SERV_RES_IDENT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies type of identifier information |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE` | CHAR(200) | NOT NULL |  | Pharamcy Service Resource Identifier information |
| 10 | `VALUE_KEY` | VARCHAR(200) | NOT NULL |  | Pharmacy Identifier information (Capitolized, and Indexed) |
| 11 | `VALUE_KEY_A_NLS` | VARCHAR(800) |  |  | VALUE_KEY_A_NLS column |
| 12 | `VALUE_KEY_NLS` | VARCHAR(202) | NOT NULL |  | Pharmacy Identifier information (Capitolized, and Indexed) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

