# PERSON_PHR_RELTN

> The person personal health record relationship table relates a patient's personal health record information to a contributor system. This relationship represents the contributor systems to which a patient has elected to send their personal health record.

**Description:** Person Personal Health Record Relationship  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PHR_RELTN_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `PERSON_PHR_INFO_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person's personal health record that is related to the contributor system. This relationship represents the contributor systems to which a patient has elected to send their personal health record. |
| 4 | `PERSON_PHR_RELTN_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `PERSON_PHR_INFO_ID` | [PERSON_PHR_INFO](PERSON_PHR_INFO.md) | `PERSON_PHR_INFO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_PHR_RELTN_HIST](PERSON_PHR_RELTN_HIST.md) | `PERSON_PHR_RELTN_ID` |

