# NOMEN_ENTITY_RELTN

> Nomenclature and Diagnosis Reltns

**Description:** NOMEN ENTITY RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Activity type code of the order. It's blank for non-order related relationships. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CHILD_ENTITY_ID` | DOUBLE | NOT NULL |  | The Cerner internal id number of the entity that is getting related to the nomenclature item |
| 5 | `CHILD_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Table Name of the Child_Entity_id |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FREETEXT_DISPLAY` | VARCHAR(255) |  |  | Free-text descripion of the generic entity item |
| 9 | `INACTIVE_ORDER_ACTION_SEQUENCE` | DOUBLE |  |  | This is the action_sequence column in table Order_Action. It is used to indicate that the relationship of the Order_Action table to the Diagnosis table is inactivated by this particular Order_Action_Sequence. |
| 10 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the nomenclature item being related |
| 11 | `NOMEN_ENTITY_RELTN_ID` | DOUBLE | NOT NULL |  | Unique Identifier for the relation |
| 12 | `ORDER_ACTION_SEQUENCE` | DOUBLE |  |  | This is the action_sequence column in table Order_Action. It is used to indicate that the relationship to the Diagnosis table is associated to a particular order action as opposed to an entire order. |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Cerner internal id number for the nomenclature item |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The table for the parent_entity_id |
| 15 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 16 | `PRIORITY` | DOUBLE |  |  | The priority of the relationships. |
| 17 | `RELTN_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Supports the ability to further define a relationship. For example, the reltn_type_cd will specify that a diagnosis is being related to another diagnosis. The reltn_subtype_cd will specify that nature of that relationship, i.e. caused by, complication of, etc. |
| 18 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Relation type between parent_entity and child_entity |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

