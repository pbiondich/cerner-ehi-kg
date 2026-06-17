# HPD_SPECIALTY

> Stores the provider's specialty information (i.e. cardiologist)

**Description:** Healthcare Provider Directory Specialty  
**Table type:** REFERENCE  
**Primary key:** `HPD_SPECIALTY_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of the Specialization |
| 3 | `FAX_NUMBER_TXT` | VARCHAR(25) |  |  | Fax Number of the Specialization |
| 4 | `HPD_SPECIALTY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the logical domain of the specialty |
| 6 | `MOBILE_NUMBER_TXT` | VARCHAR(25) |  |  | Mobile Number of the Specialization |
| 7 | `PAGER_NUMBER_TXT` | VARCHAR(25) |  |  | Pager Number of the Specialization |
| 8 | `REVISION_NBR` | DOUBLE | NOT NULL |  | Current revision of the table. This should be incremented 1 higher than the highest revision on the table. All rows in the same update should have the same revision. |
| 9 | `SPECIALTY_NAME` | VARCHAR(100) | NOT NULL |  | Name of the Organization's or Provider's Specialty |
| 10 | `TELEPHONE_NUMBER_TXT` | VARCHAR(25) |  |  | Telephone Number of the Specialization |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HPD_MEMBER_SPECIALTY_RELTN](HPD_MEMBER_SPECIALTY_RELTN.md) | `HPD_SPECIALTY_ID` |

