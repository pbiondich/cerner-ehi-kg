# PIE_EXT_SOURCE

> This table will store external sources that are configured through trust model

**Description:** External Source Schema  
**Table type:** REFERENCE  
**Primary key:** `PIE_EXT_SOURCE_ID`  
**Columns:** 9  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 2 | `PIE_EXT_SOURCE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `SOURCE_TYPE_TXT` | VARCHAR(255) | NOT NULL |  | Source Type Text with one of the value OID, CLIENT_ID or PERSONA |
| 4 | `SOURCE_TYPE_VALUE` | VARCHAR(500) | NOT NULL |  | Value of the source type |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PIE_EXT_SOURCE_CONCEPT](PIE_EXT_SOURCE_CONCEPT.md) | `PIE_EXT_SOURCE_ID` |
| [PIE_EXT_SOURCE_EXCEPTION](PIE_EXT_SOURCE_EXCEPTION.md) | `CHILD_EXT_SOURCE_ID` |
| [PIE_EXT_SOURCE_EXCEPTION](PIE_EXT_SOURCE_EXCEPTION.md) | `PARENT_EXT_SOURCE_ID` |
| [PIE_EXT_SOURCE_INFO](PIE_EXT_SOURCE_INFO.md) | `PIE_EXT_SOURCE_ID` |

