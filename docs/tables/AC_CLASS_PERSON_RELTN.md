# AC_CLASS_PERSON_RELTN

> Identifies classifications that apply to a person and how the classifications relate to one another.

**Description:** Ambulatory Care Classification Person Relation  
**Table type:** ACTIVITY  
**Primary key:** `AC_CLASS_PERSON_RELTN_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AC_CLASS_DEF_ID` | DOUBLE | NOT NULL | FK→ | The classification that this person is grouped under. |
| 3 | `AC_CLASS_PERSON_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the AC_CLASS_PERSON_RELTN table. |
| 4 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row is considered to be valid for use. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `INDEPENDENT_PARENT_IND` | DOUBLE | NOT NULL |  | Indicates if this level is tracked independently. |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location for this person and classification. |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization associated with this person and classification. |
| 9 | `PARENT_CLASS_PERSON_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The parent relationship of this person and classification. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person assigned to this classification. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AC_CLASS_DEF_ID` | [AC_CLASS_DEF](AC_CLASS_DEF.md) | `AC_CLASS_DEF_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PARENT_CLASS_PERSON_RELTN_ID` | [AC_CLASS_PERSON_RELTN](AC_CLASS_PERSON_RELTN.md) | `AC_CLASS_PERSON_RELTN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AC_CLASS_PERSON_RELTN](AC_CLASS_PERSON_RELTN.md) | `PARENT_CLASS_PERSON_RELTN_ID` |

