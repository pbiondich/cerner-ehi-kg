# SCR_PARAGRAPH_TYPE

> Each of these many be included in many patterns.

**Description:** Contains an entry for each paragraph type.  
**Table type:** REFERENCE  
**Primary key:** `SCR_PARAGRAPH_TYPE_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CANONICAL_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | Defines a SCR Pattern |
| 6 | `CKI_IDENTIFIER` | VARCHAR(50) |  |  | External identifier for this pattern, used in CKI_SOURCE to form a uniqe external identifier. |
| 7 | `CKI_SOURCE` | CHAR(12) |  |  | External source for this pattern, used in CKI_IDENTIFIER to form a uniqe external identifier. |
| 8 | `DEFAULT_CD` | DOUBLE | NOT NULL |  | Default Code |
| 9 | `DESCRIPTION` | VARCHAR(60) |  |  | Description of paragraph |
| 10 | `DISPLAY` | VARCHAR(40) |  |  | Display Text |
| 11 | `DISPLAY_KEY` | VARCHAR(40) |  |  | KEY value of DISPLAY field |
| 12 | `PARAGRAPH_CLASS_CD` | DOUBLE | NOT NULL |  | paragraph class code |
| 13 | `SCR_PARAGRAPH_TYPE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 14 | `SEQUENCE_NUMBER` | DOUBLE |  |  | Master Sequence for paragraphs |
| 15 | `TEXT_FORMAT_RULE_CD` | DOUBLE | NOT NULL |  | Text generation rule |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CANONICAL_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SCD_PARAGRAPH](SCD_PARAGRAPH.md) | `SCR_PARAGRAPH_TYPE_ID` |
| [SCR_PARAGRAPH](SCR_PARAGRAPH.md) | `SCR_PARAGRAPH_TYPE_ID` |

