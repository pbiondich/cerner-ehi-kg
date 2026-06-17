# DS_TAG

> Defines value for the given tag type from DS_TAG_TYPE. Values for TAG_TYPE -region- could be like EAST or WEST.

**Description:** Directroy Search Tag  
**Table type:** ACTIVITY  
**Primary key:** `DS_TAG_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DS_TAG_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `DS_TAG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key relationship value from DS_TAG_TYPE table |
| 3 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 4 | `TAG_TXT` | VARCHAR(255) | NOT NULL |  | The textual Value of the TAG |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DS_TAG_TYPE_ID` | [DS_TAG_TYPE](DS_TAG_TYPE.md) | `DS_TAG_TYPE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DS_TAG_ENTITY_RELTN](DS_TAG_ENTITY_RELTN.md) | `DS_TAG_ID` |

