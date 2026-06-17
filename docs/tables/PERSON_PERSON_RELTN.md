# PERSON_PERSON_RELTN

> The person-person relationship table contains pointers to other related persons in the person table(i.e., family members, etc.). The kind of relationship and genetic indication defines how the two persons are related.

**Description:** Person Person Relationship  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PERSON_RELTN_ID`  
**Columns:** 34  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTACT_ROLE_CD` | DOUBLE | NOT NULL |  | Identifies what type of role the contact person is. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `COPY_CORRESPONDENCE_CD` | DOUBLE | NOT NULL |  | Denotes whether the related person should be copied on any correspondence to the person. |
| 9 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 10 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 11 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 12 | `DEFAULT_RELTN_IND` | DOUBLE | NOT NULL |  | Identifies whether the relationship is the default displayable Mother-Child relationship. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FAMILY_RELTN_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The specific family relationship |
| 15 | `FREE_TEXT_CD` | DOUBLE | NOT NULL |  | Future Functionality |
| 16 | `FT_REL_PERSON_NAME` | VARCHAR(100) |  |  | If free textperson relationship was built the name is displayed here |
| 17 | `GENETIC_RELATIONSHIP_IND` | DOUBLE | NOT NULL |  | Indicates whether the two people specified in the relationship are geneticly tied |
| 18 | `INTERNAL_SEQ` | DOUBLE | NOT NULL |  | Internal Person Management Sequence |
| 19 | `LIVING_WITH_IND` | DOUBLE | NOT NULL |  | Indicates whether the two persons specified in the relationship live together |
| 20 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 21 | `PERSON_PERSON_RELTN_ID` | DOUBLE | NOT NULL | PK | The identifying key of Person Person Relationship |
| 22 | `PERSON_RELTN_CD` | DOUBLE | NOT NULL |  | Person Relation Code Value |
| 23 | `PERSON_RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Code value indicating what type of relationship this is |
| 24 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Identifies an sequencing priority to be used when there is more than one related person with the same person relationship type (I.e., emergency contact) |
| 25 | `RELATED_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Related Person ID |
| 26 | `RELATED_PERSON_RELTN_CD` | DOUBLE | NOT NULL |  | Related Person Relationship Code Value |
| 27 | `RELATION_SEQ` | DOUBLE | NOT NULL |  | Zero based sequence for all person_person_reltn rows across all relation types set by the master system. Added to support he UK's PDS transactions. |
| 28 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support he UK's PDS Allocated Object Identifier. Used to help keep the UK master database in sync with Millennium. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 34 | `VISITATION_ALLOWED_CD` | DOUBLE | NOT NULL |  | Visitation Allowed Code Value |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RELATED_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_PERSON_RELTN_HIST](PERSON_PERSON_RELTN_HIST.md) | `PERSON_PERSON_RELTN_ID` |

